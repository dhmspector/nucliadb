# Copyright (C) 2021 Bosutech XXI S.L.
#
# nucliadb is offered under the AGPL v3.0 and as commercial software.
# For commercial licensing, contact us at info@nuclia.com.
#
# AGPL:
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
import datetime
import math
from typing import Any, Dict, List, Optional, Tuple, Union

from nucliadb_protos.nodereader_pb2 import (
    DocumentResult,
    DocumentScored,
    DocumentSearchResponse,
    ParagraphResult,
    ParagraphSearchResponse,
    RelationSearchRequest,
    RelationSearchResponse,
    SearchResponse,
    SuggestResponse,
    VectorSearchResponse,
)
from sentry_sdk import capture_message, push_scope

from nucliadb.search import logger
from nucliadb.search.search.fetch import (
    fetch_resources,
    get_labels_paragraph,
    get_labels_resource,
    get_resource_cache,
    get_resource_from_cache,
    get_seconds_paragraph,
    get_text_paragraph,
    get_text_sentence,
)
from nucliadb_models.common import FieldTypeName
from nucliadb_models.resource import ExtractedDataTypeName
from nucliadb_models.search import (
    DirectionalRelation,
    EntitySubgraph,
    KnowledgeboxSearchResults,
    KnowledgeboxSuggestResults,
    Paragraph,
    Paragraphs,
    RelatedEntities,
    RelationDirection,
    Relations,
    ResourceProperties,
    ResourceResult,
    Resources,
    ResourceSearchResults,
    Sentence,
    Sentences,
    SortField,
    SortOptions,
    SortOrder,
    TextPosition,
)

Bm25Score = Tuple[int, int]
TimestampScore = datetime.datetime
TitleScore = str
Score = Union[Bm25Score, TimestampScore, TitleScore]


def sort_results_by_score(results: Union[List[ParagraphResult], List[DocumentResult]]):
    results.sort(key=lambda x: (x.score.bm25, x.score.booster), reverse=True)


async def text_score(
    item: Union[DocumentResult, ParagraphResult],
    sort: Optional[SortOptions],
    kbid: str,
):
    score: Any = (item.score.bm25, item.score.booster)
    if sort is None:
        return score
    resource = await get_resource_from_cache(kbid, item.uuid)
    if resource is None:
        return score
    basic = await resource.get_basic()
    if basic is None:
        return score

    if sort.field == SortField.CREATED:
        score = basic.created.ToDatetime()
    elif sort.field == SortField.MODIFIED:
        score = basic.modified.ToDatetime()
    elif sort.field == SortField.TITLE:
        score = basic.title

    return score


async def merge_documents_results(
    document_responses: List[DocumentSearchResponse],
    resources: List[str],
    count: int,
    page: int,
    kbid: str,
    sort: Optional[SortOptions] = None,
) -> Resources:
    raw_resource_list: List[Tuple[DocumentResult, Score]] = []
    facets: Dict[str, Any] = {}
    query = None
    total = 0
    next_page = False
    for document_response in document_responses:
        if query is None:
            query = document_response.query
        if document_response.facets:
            for key, value in document_response.facets.items():
                for facetresult in value.facetresults:
                    facets.setdefault(key, {}).setdefault(facetresult.tag, 0)
                    facets[key][facetresult.tag] += facetresult.total

        if document_response.next_page:
            next_page = True
        for result in document_response.results:
            score = await text_score(result, sort, kbid)
            raw_resource_list.append((result, score))

    sort_order = sort.order if sort is not None else SortOrder.ASC
    raw_resource_list.sort(key=lambda x: x[1], reverse=(sort_order == SortOrder.DESC))

    skip = page * count
    end = skip + count
    length = len(raw_resource_list)

    if length > end:
        next_page = True

    result_resource_list: List[ResourceResult] = []
    for result, _ in raw_resource_list[min(skip, length) : min(end, length)]:

        # /f/file

        labels = await get_labels_resource(result, kbid)
        _, field_type, field = result.field.split("/")

        result_resource_list.append(
            ResourceResult(
                score=result.score.bm25,
                rid=result.uuid,
                field=field,
                field_type=field_type,
                labels=labels,
            )
        )
        if result.uuid not in resources:
            resources.append(result.uuid)

    total = len(result_resource_list)

    return Resources(
        facets=facets,
        results=result_resource_list,
        query=query,
        total=total,
        page_number=page,
        page_size=count,
        next_page=next_page,
    )


async def merge_suggest_paragraph_results(
    suggest_responses: List[SuggestResponse],
    kbid: str,
    highlight: bool,
):

    raw_paragraph_list: List[ParagraphResult] = []
    query = None
    ematches = None
    for suggest_response in suggest_responses:
        if query is None:
            query = suggest_response.query
        if ematches is None:
            ematches = suggest_response.ematches
        for result in suggest_response.results:
            raw_paragraph_list.append(result)

    if len(suggest_responses) > 1:
        sort_results_by_score(raw_paragraph_list)

    result_paragraph_list: List[Paragraph] = []
    for result in raw_paragraph_list[:10]:
        _, field_type, field = result.field.split("/")
        text = await get_text_paragraph(
            result, kbid, highlight=highlight, ematches=ematches  # type: ignore
        )
        labels = await get_labels_paragraph(result, kbid)
        new_paragraph = Paragraph(
            score=result.score.bm25,
            rid=result.uuid,
            field_type=field_type,
            field=field,
            text=text,
            labels=labels,
            position=TextPosition(
                index=result.metadata.position.index,
                start=result.metadata.position.start,
                end=result.metadata.position.end,
                page_number=result.metadata.position.page_number,
            ),
        )
        if len(result.metadata.position.start_seconds) or len(
            result.metadata.position.end_seconds
        ):
            new_paragraph.start_seconds = list(result.metadata.position.start_seconds)
            new_paragraph.end_seconds = list(result.metadata.position.end_seconds)
        else:
            # TODO: Remove once we are sure all data has been migrated!
            seconds_positions = await get_seconds_paragraph(result, kbid)
            if seconds_positions is not None:
                new_paragraph.start_seconds = seconds_positions[0]
                new_paragraph.end_seconds = seconds_positions[1]
        result_paragraph_list.append(new_paragraph)

    return Paragraphs(results=result_paragraph_list, query=query)


async def merge_vectors_results(
    vector_responses: List[VectorSearchResponse],
    resources: List[str],
    kbid: str,
    count: int,
    page: int,
    min_score: float = 0.70,
):
    facets: Dict[str, Any] = {}
    raw_vectors_list: List[DocumentScored] = []

    for vector_response in vector_responses:
        for document in vector_response.documents:
            if document.score < min_score:
                continue
            if math.isnan(document.score):
                continue
            raw_vectors_list.append(document)

    if len(vector_responses) > 1:
        raw_vectors_list.sort(key=lambda x: x.score, reverse=True)

    skip = page * count
    end_element = skip + count
    length = len(raw_vectors_list)

    result_sentence_list: List[Sentence] = []
    for result in raw_vectors_list[min(skip, length) : min(end_element, length)]:

        id_count = result.doc_id.id.count("/")
        if id_count == 4:
            rid, field_type, field, index, position = result.doc_id.id.split("/")
            subfield = None
        elif id_count == 5:
            (
                rid,
                field_type,
                field,
                subfield,
                index,
                position,
            ) = result.doc_id.id.split("/")
        start, end = position.split("-")
        start_int = int(start)
        end_int = int(end)
        try:
            index_int = int(index)
        except ValueError:
            index_int = -1
        text = await get_text_sentence(
            rid, field_type, field, kbid, index_int, start_int, end_int, subfield
        )
        result_sentence_list.append(
            Sentence(
                score=result.score,
                rid=rid,
                field_type=field_type,
                field=field,
                text=text,
                index=index,
                position=TextPosition(start=start_int, end=end_int, index=index_int),
            )
        )
        if rid not in resources:
            resources.append(rid)

    return Sentences(
        results=result_sentence_list, facets=facets, page_number=page, page_size=count
    )


async def merge_paragraph_results(
    paragraph_responses: List[ParagraphSearchResponse],
    resources: List[str],
    kbid: str,
    count: int,
    page: int,
    highlight: bool,
    sort: Optional[SortOptions] = None,
):

    raw_paragraph_list: List[Tuple[ParagraphResult, Score]] = []
    facets: Dict[str, Any] = {}
    query = None
    next_page = False
    ematches: Optional[List[str]] = None
    for paragraph_response in paragraph_responses:
        if ematches is None:
            ematches = paragraph_response.ematches  # type: ignore
        if query is None:
            query = paragraph_response.query

        if paragraph_response.facets:
            for key, value in paragraph_response.facets.items():
                for facetresult in value.facetresults:
                    facets.setdefault(key, {}).setdefault(facetresult.tag, 0)
                    facets[key][facetresult.tag] += facetresult.total
        if paragraph_response.next_page:
            next_page = True
        for result in paragraph_response.results:
            score = await text_score(result, sort, kbid)
            raw_paragraph_list.append((result, score))

    sort_order = sort.order if sort is not None else SortOrder.ASC
    raw_paragraph_list.sort(key=lambda x: x[1], reverse=(sort_order == SortOrder.DESC))

    skip = page * count
    end = skip + count
    length = len(raw_paragraph_list)

    if length > end:
        next_page = True

    result_paragraph_list: List[Paragraph] = []
    for result, _ in raw_paragraph_list[min(skip, length) : min(end, length)]:
        _, field_type, field = result.field.split("/")
        text = await get_text_paragraph(result, kbid, highlight, ematches)
        labels = await get_labels_paragraph(result, kbid)
        new_paragraph = Paragraph(
            score=result.score.bm25,
            rid=result.uuid,
            field_type=field_type,
            field=field,
            text=text,
            labels=labels,
            position=TextPosition(
                index=result.metadata.position.index,
                start=result.metadata.position.start,
                end=result.metadata.position.end,
                page_number=result.metadata.position.page_number,
            ),
        )
        if len(result.metadata.position.start_seconds) or len(
            result.metadata.position.end_seconds
        ):
            new_paragraph.start_seconds = list(result.metadata.position.start_seconds)
            new_paragraph.end_seconds = list(result.metadata.position.end_seconds)
        else:
            # TODO: Remove once we are sure all data has been migrated!
            seconds_positions = await get_seconds_paragraph(result, kbid)
            if seconds_positions is not None:
                new_paragraph.start_seconds = seconds_positions[0]
                new_paragraph.end_seconds = seconds_positions[1]

        result_paragraph_list.append(new_paragraph)
        if new_paragraph.rid not in resources:
            resources.append(new_paragraph.rid)

    total = len(result_paragraph_list)

    return Paragraphs(
        results=result_paragraph_list,
        facets=facets,
        query=query,
        total=total,
        page_number=page,
        page_size=count,
        next_page=next_page,
    )


async def merge_relations_results(
    relations_responses: List[RelationSearchResponse], query: RelationSearchRequest
) -> Relations:
    relations = Relations(entities={}, graph=[])

    for entry_point in query.subgraph.entry_points:
        relations.entities[entry_point.value] = EntitySubgraph(related_to=[])

    for relation_response in relations_responses:
        for relation in relation_response.subgraph.relations:
            origin = relation.source.value
            destination = relation.to.value
            relation_label = relation.relation_label

            if origin in relations.entities:
                relations.entities[origin].related_to.append(
                    DirectionalRelation(
                        entity=destination,
                        relation=relation_label,
                        direction=RelationDirection.OUT,
                    )
                )
            elif destination in relations.entities:
                relations.entities[destination].related_to.append(
                    DirectionalRelation(
                        entity=origin,
                        relation=relation_label,
                        direction=RelationDirection.IN,
                    )
                )
            else:
                error_msg = "Relation search is returning an edge unrelated with queried entities"
                logger.error(error_msg)
                with push_scope() as scope:
                    scope.set_extra("relations_responses", relations_responses)
                    scope.set_extra("query", query)
                    scope.set_extra("relation", relation)
                    capture_message(error_msg, "error")

    return relations


async def merge_results(
    search_responses: List[SearchResponse],
    count: int,
    page: int,
    kbid: str,
    show: List[ResourceProperties],
    field_type_filter: List[FieldTypeName],
    extracted: List[ExtractedDataTypeName],
    sort: Optional[SortOptions],
    requested_relations: RelationSearchRequest,
    min_score: float = 0.85,
    highlight: bool = False,
) -> KnowledgeboxSearchResults:
    paragraphs = []
    documents = []
    vectors = []
    relations = []

    for response in search_responses:
        paragraphs.append(response.paragraph)
        documents.append(response.document)
        vectors.append(response.vector)
        relations.append(response.relation)

    api_results = KnowledgeboxSearchResults()

    get_resource_cache(clear=True)

    resources: List[str] = list()
    api_results.fulltext = await merge_documents_results(
        documents, resources, count, page, kbid, sort
    )

    api_results.paragraphs = await merge_paragraph_results(
        paragraphs,
        resources,
        kbid,
        count,
        page,
        highlight,
        sort,
    )

    api_results.sentences = await merge_vectors_results(
        vectors, resources, kbid, count, page, min_score=min_score
    )

    api_results.relations = await merge_relations_results(
        relations, requested_relations
    )

    api_results.resources = await fetch_resources(
        resources, kbid, show, field_type_filter, extracted
    )
    return api_results


async def merge_paragraphs_results(
    paragraph_responses: List[ParagraphSearchResponse],
    count: int,
    page: int,
    kbid: str,
    show: List[ResourceProperties],
    field_type_filter: List[FieldTypeName],
    extracted: List[ExtractedDataTypeName],
    highlight_split: bool,
) -> ResourceSearchResults:
    paragraphs = []
    for result in paragraph_responses:
        paragraphs.append(result)

    api_results = ResourceSearchResults()

    resources: List[str] = list()
    api_results.paragraphs = await merge_paragraph_results(
        paragraphs, resources, kbid, count, page, highlight=highlight_split
    )
    return api_results


async def merge_suggest_entities_results(
    suggest_responses: List[SuggestResponse],
) -> RelatedEntities:
    merge = RelatedEntities(entities=[], total=0)

    for response in suggest_responses:
        merge.entities.extend(response.entities.entities)
        merge.total += response.entities.total

    return merge


async def merge_suggest_results(
    suggest_responses: List[SuggestResponse],
    kbid: str,
    show: List[ResourceProperties],
    field_type_filter: List[FieldTypeName],
    highlight: bool = False,
) -> KnowledgeboxSuggestResults:

    api_results = KnowledgeboxSuggestResults()

    api_results.paragraphs = await merge_suggest_paragraph_results(
        suggest_responses, kbid, highlight=highlight
    )
    api_results.entities = await merge_suggest_entities_results(suggest_responses)
    return api_results
