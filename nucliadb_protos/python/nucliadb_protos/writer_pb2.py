# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nucliadb_protos/writer.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from nucliadb_protos import noderesources_pb2 as nucliadb__protos_dot_noderesources__pb2
try:
  nucliadb__protos_dot_utils__pb2 = nucliadb__protos_dot_noderesources__pb2.nucliadb__protos_dot_utils__pb2
except AttributeError:
  nucliadb__protos_dot_utils__pb2 = nucliadb__protos_dot_noderesources__pb2.nucliadb_protos.utils_pb2
from nucliadb_protos import resources_pb2 as nucliadb__protos_dot_resources__pb2
try:
  nucliadb__protos_dot_utils__pb2 = nucliadb__protos_dot_resources__pb2.nucliadb__protos_dot_utils__pb2
except AttributeError:
  nucliadb__protos_dot_utils__pb2 = nucliadb__protos_dot_resources__pb2.nucliadb_protos.utils_pb2
from nucliadb_protos import knowledgebox_pb2 as nucliadb__protos_dot_knowledgebox__pb2
try:
  nucliadb__protos_dot_utils__pb2 = nucliadb__protos_dot_knowledgebox__pb2.nucliadb__protos_dot_utils__pb2
except AttributeError:
  nucliadb__protos_dot_utils__pb2 = nucliadb__protos_dot_knowledgebox__pb2.nucliadb_protos.utils_pb2

from nucliadb_protos.noderesources_pb2 import *
from nucliadb_protos.resources_pb2 import *
from nucliadb_protos.knowledgebox_pb2 import *

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cnucliadb_protos/writer.proto\x12\tfdbwriter\x1a\x1fgoogle/protobuf/timestamp.proto\x1a#nucliadb_protos/noderesources.proto\x1a\x1fnucliadb_protos/resources.proto\x1a\"nucliadb_protos/knowledgebox.proto\"\xa8\x01\n\x05\x41udit\x12\x0c\n\x04user\x18\x01 \x01(\t\x12(\n\x04when\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06origin\x18\x03 \x01(\t\x12\'\n\x06source\x18\x04 \x01(\x0e\x32\x17.fdbwriter.Audit.Source\".\n\x06Source\x12\x08\n\x04HTTP\x10\x00\x12\r\n\tDASHBOARD\x10\x01\x12\x0b\n\x07\x44\x45SKTOP\x10\x02\"\xad\x01\n\x05\x45rror\x12\r\n\x05\x66ield\x18\x01 \x01(\t\x12(\n\nfield_type\x18\x02 \x01(\x0e\x32\x14.resources.FieldType\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12(\n\x04\x63ode\x18\x04 \x01(\x0e\x32\x1a.fdbwriter.Error.ErrorCode\"2\n\tErrorCode\x12\x0b\n\x07GENERIC\x10\x00\x12\x0b\n\x07\x45XTRACT\x10\x01\x12\x0b\n\x07PROCESS\x10\x02\"\xb3\x10\n\rBrokerMessage\x12\x0c\n\x04kbid\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x03 \x01(\t\x12\x0c\n\x04slug\x18\x04 \x01(\t\x12\x1f\n\x05\x61udit\x18\x05 \x01(\x0b\x32\x10.fdbwriter.Audit\x12\x32\n\x04type\x18\x06 \x01(\x0e\x32$.fdbwriter.BrokerMessage.MessageType\x12\x0f\n\x07multiid\x18\x07 \x01(\t\x12\x1f\n\x05\x62\x61sic\x18\x08 \x01(\x0b\x32\x10.resources.Basic\x12!\n\x06origin\x18\t \x01(\x0b\x32\x11.resources.Origin\x12\"\n\trelations\x18\n \x03(\x0b\x32\x0f.utils.Relation\x12\x42\n\rconversations\x18\x0b \x03(\x0b\x32+.fdbwriter.BrokerMessage.ConversationsEntry\x12\x36\n\x07layouts\x18\x0c \x03(\x0b\x32%.fdbwriter.BrokerMessage.LayoutsEntry\x12\x32\n\x05texts\x18\r \x03(\x0b\x32#.fdbwriter.BrokerMessage.TextsEntry\x12>\n\x0bkeywordsets\x18\x0e \x03(\x0b\x32).fdbwriter.BrokerMessage.KeywordsetsEntry\x12:\n\tdatetimes\x18\x0f \x03(\x0b\x32\'.fdbwriter.BrokerMessage.DatetimesEntry\x12\x32\n\x05links\x18\x10 \x03(\x0b\x32#.fdbwriter.BrokerMessage.LinksEntry\x12\x32\n\x05\x66iles\x18\x11 \x03(\x0b\x32#.fdbwriter.BrokerMessage.FilesEntry\x12\x39\n\x13link_extracted_data\x18\x12 \x03(\x0b\x32\x1c.resources.LinkExtractedData\x12\x39\n\x13\x66ile_extracted_data\x18\x13 \x03(\x0b\x32\x1c.resources.FileExtractedData\x12\x37\n\x0e\x65xtracted_text\x18\x14 \x03(\x0b\x32\x1f.resources.ExtractedTextWrapper\x12?\n\x0e\x66ield_metadata\x18\x15 \x03(\x0b\x32\'.resources.FieldComputedMetadataWrapper\x12\x39\n\rfield_vectors\x18\x16 \x03(\x0b\x32\".resources.ExtractedVectorsWrapper\x12\x45\n\x14\x66ield_large_metadata\x18\x17 \x03(\x0b\x32\'.resources.LargeComputedMetadataWrapper\x12)\n\rdelete_fields\x18\x18 \x03(\x0b\x32\x12.resources.FieldID\x12\x12\n\norigin_seq\x18\x19 \x01(\x05\x12\x1c\n\x14slow_processing_time\x18\x1a \x01(\x02\x12\x1b\n\x13pre_processing_time\x18\x1c \x01(\x02\x12-\n\tdone_time\x18\x1d \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x07txseqid\x18\x1e \x01(\x03\x42\x02\x18\x01\x12 \n\x06\x65rrors\x18\x1f \x03(\x0b\x32\x10.fdbwriter.Error\x12\x15\n\rprocessing_id\x18  \x01(\t\x12\x36\n\x06source\x18! \x01(\x0e\x32&.fdbwriter.BrokerMessage.MessageSource\x12\x13\n\x0b\x61\x63\x63ount_seq\x18\" \x01(\x03\x12\x33\n\x0cuser_vectors\x18# \x03(\x0b\x32\x1d.resources.UserVectorsWrapper\x12\x0f\n\x07reindex\x18$ \x01(\x08\x12\x1f\n\x05\x65xtra\x18% \x01(\x0b\x32\x10.resources.Extra\x1aM\n\x12\x43onversationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.resources.Conversation:\x02\x38\x01\x1a\x46\n\x0cLayoutsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.resources.FieldLayout:\x02\x38\x01\x1a\x42\n\nTextsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.resources.FieldText:\x02\x38\x01\x1aN\n\x10KeywordsetsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.resources.FieldKeywordset:\x02\x38\x01\x1aJ\n\x0e\x44\x61tetimesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\'\n\x05value\x18\x02 \x01(\x0b\x32\x18.resources.FieldDatetime:\x02\x38\x01\x1a\x42\n\nLinksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.resources.FieldLink:\x02\x38\x01\x1a\x42\n\nFilesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.resources.FieldFile:\x02\x38\x01\"N\n\x0bMessageType\x12\x0e\n\nAUTOCOMMIT\x10\x00\x12\t\n\x05MULTI\x10\x01\x12\n\n\x06\x43OMMIT\x10\x02\x12\x0c\n\x08ROLLBACK\x10\x03\x12\n\n\x06\x44\x45LETE\x10\x04\"*\n\rMessageSource\x12\n\n\x06WRITER\x10\x00\x12\r\n\tPROCESSOR\x10\x01\"\x97\x01\n\x14WriterStatusResponse\x12\x16\n\x0eknowledgeboxes\x18\x01 \x03(\t\x12\x39\n\x05msgid\x18\x02 \x03(\x0b\x32*.fdbwriter.WriterStatusResponse.MsgidEntry\x1a,\n\nMsgidEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\"\x15\n\x13WriterStatusRequest\"r\n\x10SetLabelsRequest\x12(\n\x02kb\x18\x01 \x01(\x0b\x32\x1c.knowledgebox.KnowledgeBoxID\x12\n\n\x02id\x18\x02 \x01(\t\x12(\n\x08labelset\x18\x03 \x01(\x0b\x32\x16.knowledgebox.LabelSet\"H\n\x10\x44\x65lLabelsRequest\x12(\n\x02kb\x18\x01 \x01(\x0b\x32\x1c.knowledgebox.KnowledgeBoxID\x12\n\n\x02id\x18\x02 \x01(\t\"\xb8\x01\n\x11GetLabelsResponse\x12(\n\x02kb\x18\x01 \x01(\x0b\x32\x1c.knowledgebox.KnowledgeBoxID\x12$\n\x06labels\x18\x02 \x01(\x0b\x32\x14.knowledgebox.Labels\x12\x33\n\x06status\x18\x03 \x01(\x0e\x32#.fdbwriter.GetLabelsResponse.Status\"\x1e\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\x0c\n\x08NOTFOUND\x10\x01\"<\n\x10GetLabelsRequest\x12(\n\x02kb\x18\x01 \x01(\x0b\x32\x1c.knowledgebox.KnowledgeBoxID\"\x81\x01\n\x17NewEntitiesGroupRequest\x12(\n\x02kb\x18\x01 \x01(\x0b\x32\x1c.knowledgebox.KnowledgeBoxID\x12\r\n\x05group\x18\x02 \x01(\t\x12-\n\x08\x65ntities\x18\x03 \x01(\x0b\x32\x1b.knowledgebox.EntitiesGroup\"\x99\x01\n\x18NewEntitiesGroupResponse\x12:\n\x06status\x18\x01 \x01(\x0e\x32*.fdbwriter.NewEntitiesGroupResponse.Status\"A\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x12\x10\n\x0cKB_NOT_FOUND\x10\x02\x12\x12\n\x0e\x41LREADY_EXISTS\x10\x03\"|\n\x12SetEntitiesRequest\x12(\n\x02kb\x18\x01 \x01(\x0b\x32\x1c.knowledgebox.KnowledgeBoxID\x12\r\n\x05group\x18\x02 \x01(\t\x12-\n\x08\x65ntities\x18\x03 \x01(\x0b\x32\x1b.knowledgebox.EntitiesGroup\"\x8a\x03\n\x1aUpdateEntitiesGroupRequest\x12(\n\x02kb\x18\x01 \x01(\x0b\x32\x1c.knowledgebox.KnowledgeBoxID\x12\r\n\x05group\x18\x02 \x01(\t\x12;\n\x03\x61\x64\x64\x18\x03 \x03(\x0b\x32..fdbwriter.UpdateEntitiesGroupRequest.AddEntry\x12\x41\n\x06update\x18\x04 \x03(\x0b\x32\x31.fdbwriter.UpdateEntitiesGroupRequest.UpdateEntry\x12\x0e\n\x06\x64\x65lete\x18\x05 \x03(\t\x12\r\n\x05title\x18\x06 \x01(\t\x12\r\n\x05\x63olor\x18\x07 \x01(\t\x1a@\n\x08\x41\x64\x64\x45ntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.knowledgebox.Entity:\x02\x38\x01\x1a\x43\n\x0bUpdateEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.knowledgebox.Entity:\x02\x38\x01\"\xa9\x01\n\x1bUpdateEntitiesGroupResponse\x12=\n\x06status\x18\x01 \x01(\x0e\x32-.fdbwriter.UpdateEntitiesGroupResponse.Status\"K\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x12\x10\n\x0cKB_NOT_FOUND\x10\x02\x12\x1c\n\x18\x45NTITIES_GROUP_NOT_FOUND\x10\x03\"E\n\x19ListEntitiesGroupsRequest\x12(\n\x02kb\x18\x01 \x01(\x0b\x32\x1c.knowledgebox.KnowledgeBoxID\"\x9b\x02\n\x1aListEntitiesGroupsResponse\x12\x41\n\x06groups\x18\x01 \x03(\x0b\x32\x31.fdbwriter.ListEntitiesGroupsResponse.GroupsEntry\x12<\n\x06status\x18\x02 \x01(\x0e\x32,.fdbwriter.ListEntitiesGroupsResponse.Status\x1aQ\n\x0bGroupsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x31\n\x05value\x18\x02 \x01(\x0b\x32\".knowledgebox.EntitiesGroupSummary:\x02\x38\x01\")\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\x0c\n\x08NOTFOUND\x10\x01\x12\t\n\x05\x45RROR\x10\x02\">\n\x12GetEntitiesRequest\x12(\n\x02kb\x18\x01 \x01(\x0b\x32\x1c.knowledgebox.KnowledgeBoxID\"\xa9\x02\n\x13GetEntitiesResponse\x12(\n\x02kb\x18\x01 \x01(\x0b\x32\x1c.knowledgebox.KnowledgeBoxID\x12:\n\x06groups\x18\x02 \x03(\x0b\x32*.fdbwriter.GetEntitiesResponse.GroupsEntry\x12\x35\n\x06status\x18\x03 \x01(\x0e\x32%.fdbwriter.GetEntitiesResponse.Status\x1aJ\n\x0bGroupsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x1b.knowledgebox.EntitiesGroup:\x02\x38\x01\")\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\x0c\n\x08NOTFOUND\x10\x01\x12\t\n\x05\x45RROR\x10\x02\"M\n\x12\x44\x65lEntitiesRequest\x12(\n\x02kb\x18\x01 \x01(\x0b\x32\x1c.knowledgebox.KnowledgeBoxID\x12\r\n\x05group\x18\x02 \x01(\t\"\xd9\x01\n\x14MergeEntitiesRequest\x12(\n\x02kb\x18\x01 \x01(\x0b\x32\x1c.knowledgebox.KnowledgeBoxID\x12\x36\n\x04\x66rom\x18\x02 \x01(\x0b\x32(.fdbwriter.MergeEntitiesRequest.EntityID\x12\x34\n\x02to\x18\x03 \x01(\x0b\x32(.fdbwriter.MergeEntitiesRequest.EntityID\x1a)\n\x08\x45ntityID\x12\r\n\x05group\x18\x01 \x01(\t\x12\x0e\n\x06\x65ntity\x18\x02 \x01(\t\"P\n\x12GetLabelSetRequest\x12(\n\x02kb\x18\x01 \x01(\x0b\x32\x1c.knowledgebox.KnowledgeBoxID\x12\x10\n\x08labelset\x18\x02 \x01(\t\"\xc0\x01\n\x13GetLabelSetResponse\x12(\n\x02kb\x18\x01 \x01(\x0b\x32\x1c.knowledgebox.KnowledgeBoxID\x12(\n\x08labelset\x18\x02 \x01(\x0b\x32\x16.knowledgebox.LabelSet\x12\x35\n\x06status\x18\x03 \x01(\x0e\x32%.fdbwriter.GetLabelSetResponse.Status\"\x1e\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\x0c\n\x08NOTFOUND\x10\x01\"R\n\x17GetEntitiesGroupRequest\x12(\n\x02kb\x18\x01 \x01(\x0b\x32\x1c.knowledgebox.KnowledgeBoxID\x12\r\n\x05group\x18\x02 \x01(\t\"\xf9\x01\n\x18GetEntitiesGroupResponse\x12(\n\x02kb\x18\x01 \x01(\x0b\x32\x1c.knowledgebox.KnowledgeBoxID\x12*\n\x05group\x18\x02 \x01(\x0b\x32\x1b.knowledgebox.EntitiesGroup\x12:\n\x06status\x18\x03 \x01(\x0e\x32*.fdbwriter.GetEntitiesGroupResponse.Status\"K\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\x10\n\x0cKB_NOT_FOUND\x10\x01\x12\x1c\n\x18\x45NTITIES_GROUP_NOT_FOUND\x10\x02\x12\t\n\x05\x45RROR\x10\x03\"@\n\x14GetVectorSetsRequest\x12(\n\x02kb\x18\x01 \x01(\x0b\x32\x1c.knowledgebox.KnowledgeBoxID\"\xd3\x01\n\x15GetVectorSetsResponse\x12(\n\x02kb\x18\x01 \x01(\x0b\x32\x1c.knowledgebox.KnowledgeBoxID\x12,\n\nvectorsets\x18\x02 \x01(\x0b\x32\x18.knowledgebox.VectorSets\x12\x37\n\x06status\x18\x03 \x01(\x0e\x32\'.fdbwriter.GetVectorSetsResponse.Status\")\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\x0c\n\x08NOTFOUND\x10\x01\x12\t\n\x05\x45RROR\x10\x02\"R\n\x13\x44\x65lVectorSetRequest\x12(\n\x02kb\x18\x01 \x01(\x0b\x32\x1c.knowledgebox.KnowledgeBoxID\x12\x11\n\tvectorset\x18\x02 \x01(\t\"w\n\x13SetVectorSetRequest\x12(\n\x02kb\x18\x01 \x01(\x0b\x32\x1c.knowledgebox.KnowledgeBoxID\x12\n\n\x02id\x18\x02 \x01(\t\x12*\n\tvectorset\x18\x03 \x01(\x0b\x32\x17.knowledgebox.VectorSet\"m\n\x0eOpStatusWriter\x12\x30\n\x06status\x18\x01 \x01(\x0e\x32 .fdbwriter.OpStatusWriter.Status\")\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x12\x0c\n\x08NOTFOUND\x10\x02\"\xdb\x02\n\x0cNotification\x12\x11\n\tpartition\x18\x01 \x01(\x05\x12\r\n\x05multi\x18\x02 \x01(\t\x12\x0c\n\x04uuid\x18\x03 \x01(\t\x12\x0c\n\x04kbid\x18\x04 \x01(\t\x12\r\n\x05seqid\x18\x05 \x01(\x03\x12.\n\x06\x61\x63tion\x18\x06 \x01(\x0e\x32\x1e.fdbwriter.Notification.Action\x12\x35\n\nwrite_type\x18\x07 \x01(\x0e\x32!.fdbwriter.Notification.WriteType\x12)\n\x07message\x18\x08 \x01(\x0b\x32\x18.fdbwriter.BrokerMessage\",\n\x06\x41\x63tion\x12\n\n\x06\x43OMMIT\x10\x00\x12\t\n\x05\x41\x42ORT\x10\x01\x12\x0b\n\x07INDEXED\x10\x02\">\n\tWriteType\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07\x43REATED\x10\x01\x12\x0c\n\x08MODIFIED\x10\x02\x12\x0b\n\x07\x44\x45LETED\x10\x03\"\xdf\x01\n\x06Member\x12\n\n\x02id\x18\x01 \x01(\t\x12\x16\n\x0elisten_address\x18\x02 \x01(\t\x12\x0f\n\x07is_self\x18\x03 \x01(\x08\x12$\n\x04type\x18\x04 \x01(\x0e\x32\x16.fdbwriter.Member.Type\x12\r\n\x05\x64ummy\x18\x05 \x01(\x08\x12\x16\n\nload_score\x18\x06 \x01(\x02\x42\x02\x18\x01\x12\x13\n\x0bshard_count\x18\x07 \x01(\r\">\n\x04Type\x12\x06\n\x02IO\x10\x00\x12\n\n\x06SEARCH\x10\x01\x12\n\n\x06INGEST\x10\x02\x12\t\n\x05TRAIN\x10\x03\x12\x0b\n\x07UNKNOWN\x10\x04\"\x14\n\x12ListMembersRequest\"9\n\x13ListMembersResponse\x12\"\n\x07members\x18\x01 \x03(\x0b\x32\x11.fdbwriter.Member\"H\n\x0cShardReplica\x12*\n\x05shard\x18\x01 \x01(\x0b\x32\x1b.noderesources.ShardCreated\x12\x0c\n\x04node\x18\x02 \x01(\t\"v\n\x0bShardObject\x12\r\n\x05shard\x18\x01 \x01(\t\x12)\n\x08replicas\x18\x03 \x03(\x0b\x32\x17.fdbwriter.ShardReplica\x12-\n\ttimestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"{\n\x06Shards\x12&\n\x06shards\x18\x01 \x03(\x0b\x32\x16.fdbwriter.ShardObject\x12\x0c\n\x04kbid\x18\x02 \x01(\t\x12\x0e\n\x06\x61\x63tual\x18\x03 \x01(\x05\x12+\n\nsimilarity\x18\x04 \x01(\x0e\x32\x17.utils.VectorSimilarity\"e\n\x0fResourceFieldId\x12\x0c\n\x04kbid\x18\x01 \x01(\t\x12\x0b\n\x03rid\x18\x02 \x01(\t\x12(\n\nfield_type\x18\x03 \x01(\x0e\x32\x14.resources.FieldType\x12\r\n\x05\x66ield\x18\x04 \x01(\t\"C\n\rIndexResource\x12\x0c\n\x04kbid\x18\x01 \x01(\t\x12\x0b\n\x03rid\x18\x02 \x01(\t\x12\x17\n\x0freindex_vectors\x18\x03 \x01(\x08\"\r\n\x0bIndexStatus\",\n\x1bResourceFieldExistsResponse\x12\r\n\x05\x66ound\x18\x01 \x01(\x08\"/\n\x11ResourceIdRequest\x12\x0c\n\x04kbid\x18\x01 \x01(\t\x12\x0c\n\x04slug\x18\x02 \x01(\t\"\"\n\x12ResourceIdResponse\x12\x0c\n\x04uuid\x18\x01 \x01(\t\"\x1d\n\rExportRequest\x12\x0c\n\x04kbid\x18\x01 \x01(\t\"w\n\x11SetVectorsRequest\x12$\n\x07vectors\x18\x01 \x01(\x0b\x32\x13.utils.VectorObject\x12\x0c\n\x04kbid\x18\x02 \x01(\t\x12\x0b\n\x03rid\x18\x03 \x01(\t\x12!\n\x05\x66ield\x18\x04 \x01(\x0b\x32\x12.resources.FieldID\"#\n\x12SetVectorsResponse\x12\r\n\x05\x66ound\x18\x01 \x01(\x08\"*\n\x0b\x46ileRequest\x12\x0e\n\x06\x62ucket\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\"\x1a\n\nBinaryData\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"a\n\x0e\x42inaryMetadata\x12\x0c\n\x04kbid\x18\x02 \x01(\t\x12\x0b\n\x03key\x18\x03 \x01(\t\x12\x0c\n\x04size\x18\x04 \x01(\x05\x12\x10\n\x08\x66ilename\x18\x05 \x01(\t\x12\x14\n\x0c\x63ontent_type\x18\x06 \x01(\t\"k\n\x10UploadBinaryData\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\x12-\n\x08metadata\x18\x02 \x01(\x0b\x32\x19.fdbwriter.BinaryMetadataH\x00\x12\x11\n\x07payload\x18\x03 \x01(\x0cH\x00\x42\x06\n\x04\x64\x61ta\"\x0e\n\x0c\x46ileUploaded\"\x1f\n\x0fSynonymsRequest\x12\x0c\n\x04kbid\x18\x01 \x01(\t\"j\n\x12SetSynonymsRequest\x12*\n\x04kbid\x18\x01 \x01(\x0b\x32\x1c.knowledgebox.KnowledgeBoxID\x12(\n\x08synonyms\x18\x02 \x01(\x0b\x32\x16.knowledgebox.Synonyms\"j\n\x13GetSynonymsResponse\x12)\n\x06status\x18\x01 \x01(\x0b\x32\x19.fdbwriter.OpStatusWriter\x12(\n\x08synonyms\x18\x02 \x01(\x0b\x32\x16.knowledgebox.Synonyms2\xab\x16\n\x06Writer\x12M\n\x0fGetKnowledgeBox\x12\x1c.knowledgebox.KnowledgeBoxID\x1a\x1a.knowledgebox.KnowledgeBox\"\x00\x12Y\n\x0fNewKnowledgeBox\x12\x1d.knowledgebox.KnowledgeBoxNew\x1a%.knowledgebox.NewKnowledgeBoxResponse\"\x00\x12^\n\x12\x44\x65leteKnowledgeBox\x12\x1c.knowledgebox.KnowledgeBoxID\x1a(.knowledgebox.DeleteKnowledgeBoxResponse\"\x00\x12\x62\n\x12UpdateKnowledgeBox\x12 .knowledgebox.KnowledgeBoxUpdate\x1a(.knowledgebox.UpdateKnowledgeBoxResponse\"\x00\x12m\n CleanAndUpgradeKnowledgeBoxIndex\x12\x1c.knowledgebox.KnowledgeBoxID\x1a).knowledgebox.CleanedKnowledgeBoxResponse\"\x00\x12V\n\x10ListKnowledgeBox\x12 .knowledgebox.KnowledgeBoxPrefix\x1a\x1c.knowledgebox.KnowledgeBoxID\"\x00\x30\x01\x12V\n\x0eGCKnowledgeBox\x12\x1c.knowledgebox.KnowledgeBoxID\x1a$.knowledgebox.GCKnowledgeBoxResponse\"\x00\x12K\n\nSetVectors\x12\x1c.fdbwriter.SetVectorsRequest\x1a\x1d.fdbwriter.SetVectorsResponse\"\x00\x12[\n\x13ResourceFieldExists\x12\x1a.fdbwriter.ResourceFieldId\x1a&.fdbwriter.ResourceFieldExistsResponse\"\x00\x12N\n\rGetResourceId\x12\x1c.fdbwriter.ResourceIdRequest\x1a\x1d.fdbwriter.ResourceIdResponse\"\x00\x12I\n\x0eProcessMessage\x12\x18.fdbwriter.BrokerMessage\x1a\x19.fdbwriter.OpStatusWriter\"\x00(\x01\x12H\n\tGetLabels\x12\x1b.fdbwriter.GetLabelsRequest\x1a\x1c.fdbwriter.GetLabelsResponse\"\x00\x12N\n\x0bGetLabelSet\x12\x1d.fdbwriter.GetLabelSetRequest\x1a\x1e.fdbwriter.GetLabelSetResponse\"\x00\x12\x45\n\tSetLabels\x12\x1b.fdbwriter.SetLabelsRequest\x1a\x19.fdbwriter.OpStatusWriter\"\x00\x12\x45\n\tDelLabels\x12\x1b.fdbwriter.DelLabelsRequest\x1a\x19.fdbwriter.OpStatusWriter\"\x00\x12T\n\rGetVectorSets\x12\x1f.fdbwriter.GetVectorSetsRequest\x1a .fdbwriter.GetVectorSetsResponse\"\x00\x12K\n\x0c\x44\x65lVectorSet\x12\x1e.fdbwriter.DelVectorSetRequest\x1a\x19.fdbwriter.OpStatusWriter\"\x00\x12K\n\x0cSetVectorSet\x12\x1e.fdbwriter.SetVectorSetRequest\x1a\x19.fdbwriter.OpStatusWriter\"\x00\x12]\n\x10NewEntitiesGroup\x12\".fdbwriter.NewEntitiesGroupRequest\x1a#.fdbwriter.NewEntitiesGroupResponse\"\x00\x12N\n\x0bGetEntities\x12\x1d.fdbwriter.GetEntitiesRequest\x1a\x1e.fdbwriter.GetEntitiesResponse\"\x00\x12]\n\x10GetEntitiesGroup\x12\".fdbwriter.GetEntitiesGroupRequest\x1a#.fdbwriter.GetEntitiesGroupResponse\"\x00\x12\x63\n\x12ListEntitiesGroups\x12$.fdbwriter.ListEntitiesGroupsRequest\x1a%.fdbwriter.ListEntitiesGroupsResponse\"\x00\x12I\n\x0bSetEntities\x12\x1d.fdbwriter.SetEntitiesRequest\x1a\x19.fdbwriter.OpStatusWriter\"\x00\x12\x66\n\x13UpdateEntitiesGroup\x12%.fdbwriter.UpdateEntitiesGroupRequest\x1a&.fdbwriter.UpdateEntitiesGroupResponse\"\x00\x12I\n\x0b\x44\x65lEntities\x12\x1d.fdbwriter.DelEntitiesRequest\x1a\x19.fdbwriter.OpStatusWriter\"\x00\x12M\n\x0bGetSynonyms\x12\x1c.knowledgebox.KnowledgeBoxID\x1a\x1e.fdbwriter.GetSynonymsResponse\"\x00\x12I\n\x0bSetSynonyms\x12\x1d.fdbwriter.SetSynonymsRequest\x1a\x19.fdbwriter.OpStatusWriter\"\x00\x12H\n\x0b\x44\x65lSynonyms\x12\x1c.knowledgebox.KnowledgeBoxID\x1a\x19.fdbwriter.OpStatusWriter\"\x00\x12K\n\x06Status\x12\x1e.fdbwriter.WriterStatusRequest\x1a\x1f.fdbwriter.WriterStatusResponse\"\x00\x12L\n\x0bListMembers\x12\x1d.fdbwriter.ListMembersRequest\x1a\x1e.fdbwriter.ListMembersResponse\x12;\n\x05Index\x12\x18.fdbwriter.IndexResource\x1a\x16.fdbwriter.IndexStatus\"\x00\x12=\n\x07ReIndex\x12\x18.fdbwriter.IndexResource\x1a\x16.fdbwriter.IndexStatus\"\x00\x12@\n\x06\x45xport\x12\x18.fdbwriter.ExportRequest\x1a\x18.fdbwriter.BrokerMessage\"\x00\x30\x01\x12\x41\n\x0c\x44ownloadFile\x12\x16.fdbwriter.FileRequest\x1a\x15.fdbwriter.BinaryData\"\x00\x30\x01\x12\x46\n\nUploadFile\x12\x1b.fdbwriter.UploadBinaryData\x1a\x17.fdbwriter.FileUploaded\"\x00(\x01P\x01P\x02P\x03\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nucliadb_protos.writer_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BROKERMESSAGE_CONVERSATIONSENTRY._options = None
  _BROKERMESSAGE_CONVERSATIONSENTRY._serialized_options = b'8\001'
  _BROKERMESSAGE_LAYOUTSENTRY._options = None
  _BROKERMESSAGE_LAYOUTSENTRY._serialized_options = b'8\001'
  _BROKERMESSAGE_TEXTSENTRY._options = None
  _BROKERMESSAGE_TEXTSENTRY._serialized_options = b'8\001'
  _BROKERMESSAGE_KEYWORDSETSENTRY._options = None
  _BROKERMESSAGE_KEYWORDSETSENTRY._serialized_options = b'8\001'
  _BROKERMESSAGE_DATETIMESENTRY._options = None
  _BROKERMESSAGE_DATETIMESENTRY._serialized_options = b'8\001'
  _BROKERMESSAGE_LINKSENTRY._options = None
  _BROKERMESSAGE_LINKSENTRY._serialized_options = b'8\001'
  _BROKERMESSAGE_FILESENTRY._options = None
  _BROKERMESSAGE_FILESENTRY._serialized_options = b'8\001'
  _BROKERMESSAGE.fields_by_name['txseqid']._options = None
  _BROKERMESSAGE.fields_by_name['txseqid']._serialized_options = b'\030\001'
  _WRITERSTATUSRESPONSE_MSGIDENTRY._options = None
  _WRITERSTATUSRESPONSE_MSGIDENTRY._serialized_options = b'8\001'
  _UPDATEENTITIESGROUPREQUEST_ADDENTRY._options = None
  _UPDATEENTITIESGROUPREQUEST_ADDENTRY._serialized_options = b'8\001'
  _UPDATEENTITIESGROUPREQUEST_UPDATEENTRY._options = None
  _UPDATEENTITIESGROUPREQUEST_UPDATEENTRY._serialized_options = b'8\001'
  _LISTENTITIESGROUPSRESPONSE_GROUPSENTRY._options = None
  _LISTENTITIESGROUPSRESPONSE_GROUPSENTRY._serialized_options = b'8\001'
  _GETENTITIESRESPONSE_GROUPSENTRY._options = None
  _GETENTITIESRESPONSE_GROUPSENTRY._serialized_options = b'8\001'
  _MEMBER.fields_by_name['load_score']._options = None
  _MEMBER.fields_by_name['load_score']._serialized_options = b'\030\001'
  _AUDIT._serialized_start=183
  _AUDIT._serialized_end=351
  _AUDIT_SOURCE._serialized_start=305
  _AUDIT_SOURCE._serialized_end=351
  _ERROR._serialized_start=354
  _ERROR._serialized_end=527
  _ERROR_ERRORCODE._serialized_start=477
  _ERROR_ERRORCODE._serialized_end=527
  _BROKERMESSAGE._serialized_start=530
  _BROKERMESSAGE._serialized_end=2629
  _BROKERMESSAGE_CONVERSATIONSENTRY._serialized_start=1996
  _BROKERMESSAGE_CONVERSATIONSENTRY._serialized_end=2073
  _BROKERMESSAGE_LAYOUTSENTRY._serialized_start=2075
  _BROKERMESSAGE_LAYOUTSENTRY._serialized_end=2145
  _BROKERMESSAGE_TEXTSENTRY._serialized_start=2147
  _BROKERMESSAGE_TEXTSENTRY._serialized_end=2213
  _BROKERMESSAGE_KEYWORDSETSENTRY._serialized_start=2215
  _BROKERMESSAGE_KEYWORDSETSENTRY._serialized_end=2293
  _BROKERMESSAGE_DATETIMESENTRY._serialized_start=2295
  _BROKERMESSAGE_DATETIMESENTRY._serialized_end=2369
  _BROKERMESSAGE_LINKSENTRY._serialized_start=2371
  _BROKERMESSAGE_LINKSENTRY._serialized_end=2437
  _BROKERMESSAGE_FILESENTRY._serialized_start=2439
  _BROKERMESSAGE_FILESENTRY._serialized_end=2505
  _BROKERMESSAGE_MESSAGETYPE._serialized_start=2507
  _BROKERMESSAGE_MESSAGETYPE._serialized_end=2585
  _BROKERMESSAGE_MESSAGESOURCE._serialized_start=2587
  _BROKERMESSAGE_MESSAGESOURCE._serialized_end=2629
  _WRITERSTATUSRESPONSE._serialized_start=2632
  _WRITERSTATUSRESPONSE._serialized_end=2783
  _WRITERSTATUSRESPONSE_MSGIDENTRY._serialized_start=2739
  _WRITERSTATUSRESPONSE_MSGIDENTRY._serialized_end=2783
  _WRITERSTATUSREQUEST._serialized_start=2785
  _WRITERSTATUSREQUEST._serialized_end=2806
  _SETLABELSREQUEST._serialized_start=2808
  _SETLABELSREQUEST._serialized_end=2922
  _DELLABELSREQUEST._serialized_start=2924
  _DELLABELSREQUEST._serialized_end=2996
  _GETLABELSRESPONSE._serialized_start=2999
  _GETLABELSRESPONSE._serialized_end=3183
  _GETLABELSRESPONSE_STATUS._serialized_start=3153
  _GETLABELSRESPONSE_STATUS._serialized_end=3183
  _GETLABELSREQUEST._serialized_start=3185
  _GETLABELSREQUEST._serialized_end=3245
  _NEWENTITIESGROUPREQUEST._serialized_start=3248
  _NEWENTITIESGROUPREQUEST._serialized_end=3377
  _NEWENTITIESGROUPRESPONSE._serialized_start=3380
  _NEWENTITIESGROUPRESPONSE._serialized_end=3533
  _NEWENTITIESGROUPRESPONSE_STATUS._serialized_start=3468
  _NEWENTITIESGROUPRESPONSE_STATUS._serialized_end=3533
  _SETENTITIESREQUEST._serialized_start=3535
  _SETENTITIESREQUEST._serialized_end=3659
  _UPDATEENTITIESGROUPREQUEST._serialized_start=3662
  _UPDATEENTITIESGROUPREQUEST._serialized_end=4056
  _UPDATEENTITIESGROUPREQUEST_ADDENTRY._serialized_start=3923
  _UPDATEENTITIESGROUPREQUEST_ADDENTRY._serialized_end=3987
  _UPDATEENTITIESGROUPREQUEST_UPDATEENTRY._serialized_start=3989
  _UPDATEENTITIESGROUPREQUEST_UPDATEENTRY._serialized_end=4056
  _UPDATEENTITIESGROUPRESPONSE._serialized_start=4059
  _UPDATEENTITIESGROUPRESPONSE._serialized_end=4228
  _UPDATEENTITIESGROUPRESPONSE_STATUS._serialized_start=4153
  _UPDATEENTITIESGROUPRESPONSE_STATUS._serialized_end=4228
  _LISTENTITIESGROUPSREQUEST._serialized_start=4230
  _LISTENTITIESGROUPSREQUEST._serialized_end=4299
  _LISTENTITIESGROUPSRESPONSE._serialized_start=4302
  _LISTENTITIESGROUPSRESPONSE._serialized_end=4585
  _LISTENTITIESGROUPSRESPONSE_GROUPSENTRY._serialized_start=4461
  _LISTENTITIESGROUPSRESPONSE_GROUPSENTRY._serialized_end=4542
  _LISTENTITIESGROUPSRESPONSE_STATUS._serialized_start=4544
  _LISTENTITIESGROUPSRESPONSE_STATUS._serialized_end=4585
  _GETENTITIESREQUEST._serialized_start=4587
  _GETENTITIESREQUEST._serialized_end=4649
  _GETENTITIESRESPONSE._serialized_start=4652
  _GETENTITIESRESPONSE._serialized_end=4949
  _GETENTITIESRESPONSE_GROUPSENTRY._serialized_start=4832
  _GETENTITIESRESPONSE_GROUPSENTRY._serialized_end=4906
  _GETENTITIESRESPONSE_STATUS._serialized_start=4544
  _GETENTITIESRESPONSE_STATUS._serialized_end=4585
  _DELENTITIESREQUEST._serialized_start=4951
  _DELENTITIESREQUEST._serialized_end=5028
  _MERGEENTITIESREQUEST._serialized_start=5031
  _MERGEENTITIESREQUEST._serialized_end=5248
  _MERGEENTITIESREQUEST_ENTITYID._serialized_start=5207
  _MERGEENTITIESREQUEST_ENTITYID._serialized_end=5248
  _GETLABELSETREQUEST._serialized_start=5250
  _GETLABELSETREQUEST._serialized_end=5330
  _GETLABELSETRESPONSE._serialized_start=5333
  _GETLABELSETRESPONSE._serialized_end=5525
  _GETLABELSETRESPONSE_STATUS._serialized_start=3153
  _GETLABELSETRESPONSE_STATUS._serialized_end=3183
  _GETENTITIESGROUPREQUEST._serialized_start=5527
  _GETENTITIESGROUPREQUEST._serialized_end=5609
  _GETENTITIESGROUPRESPONSE._serialized_start=5612
  _GETENTITIESGROUPRESPONSE._serialized_end=5861
  _GETENTITIESGROUPRESPONSE_STATUS._serialized_start=5786
  _GETENTITIESGROUPRESPONSE_STATUS._serialized_end=5861
  _GETVECTORSETSREQUEST._serialized_start=5863
  _GETVECTORSETSREQUEST._serialized_end=5927
  _GETVECTORSETSRESPONSE._serialized_start=5930
  _GETVECTORSETSRESPONSE._serialized_end=6141
  _GETVECTORSETSRESPONSE_STATUS._serialized_start=4544
  _GETVECTORSETSRESPONSE_STATUS._serialized_end=4585
  _DELVECTORSETREQUEST._serialized_start=6143
  _DELVECTORSETREQUEST._serialized_end=6225
  _SETVECTORSETREQUEST._serialized_start=6227
  _SETVECTORSETREQUEST._serialized_end=6346
  _OPSTATUSWRITER._serialized_start=6348
  _OPSTATUSWRITER._serialized_end=6457
  _OPSTATUSWRITER_STATUS._serialized_start=6416
  _OPSTATUSWRITER_STATUS._serialized_end=6457
  _NOTIFICATION._serialized_start=6460
  _NOTIFICATION._serialized_end=6807
  _NOTIFICATION_ACTION._serialized_start=6699
  _NOTIFICATION_ACTION._serialized_end=6743
  _NOTIFICATION_WRITETYPE._serialized_start=6745
  _NOTIFICATION_WRITETYPE._serialized_end=6807
  _MEMBER._serialized_start=6810
  _MEMBER._serialized_end=7033
  _MEMBER_TYPE._serialized_start=6971
  _MEMBER_TYPE._serialized_end=7033
  _LISTMEMBERSREQUEST._serialized_start=7035
  _LISTMEMBERSREQUEST._serialized_end=7055
  _LISTMEMBERSRESPONSE._serialized_start=7057
  _LISTMEMBERSRESPONSE._serialized_end=7114
  _SHARDREPLICA._serialized_start=7116
  _SHARDREPLICA._serialized_end=7188
  _SHARDOBJECT._serialized_start=7190
  _SHARDOBJECT._serialized_end=7308
  _SHARDS._serialized_start=7310
  _SHARDS._serialized_end=7433
  _RESOURCEFIELDID._serialized_start=7435
  _RESOURCEFIELDID._serialized_end=7536
  _INDEXRESOURCE._serialized_start=7538
  _INDEXRESOURCE._serialized_end=7605
  _INDEXSTATUS._serialized_start=7607
  _INDEXSTATUS._serialized_end=7620
  _RESOURCEFIELDEXISTSRESPONSE._serialized_start=7622
  _RESOURCEFIELDEXISTSRESPONSE._serialized_end=7666
  _RESOURCEIDREQUEST._serialized_start=7668
  _RESOURCEIDREQUEST._serialized_end=7715
  _RESOURCEIDRESPONSE._serialized_start=7717
  _RESOURCEIDRESPONSE._serialized_end=7751
  _EXPORTREQUEST._serialized_start=7753
  _EXPORTREQUEST._serialized_end=7782
  _SETVECTORSREQUEST._serialized_start=7784
  _SETVECTORSREQUEST._serialized_end=7903
  _SETVECTORSRESPONSE._serialized_start=7905
  _SETVECTORSRESPONSE._serialized_end=7940
  _FILEREQUEST._serialized_start=7942
  _FILEREQUEST._serialized_end=7984
  _BINARYDATA._serialized_start=7986
  _BINARYDATA._serialized_end=8012
  _BINARYMETADATA._serialized_start=8014
  _BINARYMETADATA._serialized_end=8111
  _UPLOADBINARYDATA._serialized_start=8113
  _UPLOADBINARYDATA._serialized_end=8220
  _FILEUPLOADED._serialized_start=8222
  _FILEUPLOADED._serialized_end=8236
  _SYNONYMSREQUEST._serialized_start=8238
  _SYNONYMSREQUEST._serialized_end=8269
  _SETSYNONYMSREQUEST._serialized_start=8271
  _SETSYNONYMSREQUEST._serialized_end=8377
  _GETSYNONYMSRESPONSE._serialized_start=8379
  _GETSYNONYMSRESPONSE._serialized_end=8485
  _WRITER._serialized_start=8488
  _WRITER._serialized_end=11347
# @@protoc_insertion_point(module_scope)
