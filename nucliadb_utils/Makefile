.PHONY: install-dev
install-dev:
## TODO: remove pip version install when pip is fixed. Right now it was making mypy fail.
	pip install --upgrade "pip<23.1"
	pip install -r ../test-requirements.txt
	pip install -r ../code-requirements.txt
	cd .. && pip install -r nucliadb_utils/requirements-sources.txt
	pip install -r requirements.txt
	pip install -e .[cache,storages,fastapi,postgres]

.PHONY: format
format:
	isort --profile black .
	black .

.PHONY: lint
lint:
	flake8 nucliadb_utils --config=setup.cfg
	isort -c --profile black .
	black --check .
	MYPYPATH=../mypy_stubs mypy --config-file=../mypy.ini .

.PHONY: test
test:
	pytest -s --tb=native -v nucliadb_utils

.PHONY: test-cov
test-cov:
	pytest -rfE --cov=nucliadb_utils --cov-config=../.coveragerc -s --tb=native -v --cov-report term-missing:skip-covered --cov-report xml nucliadb_utils
