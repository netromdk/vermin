VERMIN_FILES=vermin vermin.py
TEST_FILES=tests runtests.py
OTHER_FILES=count.py
MODULES=vermin tests
TOP_LEVEL_FILES=${MODULES} vermin.py runtests.py ${OTHER_FILES}

self-test:
	./vermin.py --violations -q -t=3 ${VERMIN_FILES}

test: self-test
	./runtests.py

test-all: self-test
	python2 ./runtests.py
	python3 ./runtests.py

count:
	./count.py
	@echo "Tests: `grep -ri 'def test_' tests | wc -l | xargs`"
	@echo "Vermin SLOC: `sloccount vermin/ vermin.py 2>/dev/null | grep 'python:' | xargs`"
	@echo "Tests  SLOC: `sloccount tests/ runtests.py 2>/dev/null | grep 'python:' | xargs`"

setup-venv: clean-venv
	virtualenv -p python3 .venv

setup-coverage: clean
	pip install -r misc/.coverage-requirements.txt

setup-analysis: clean
	pip install -r misc/.analysis-requirements.txt

setup: setup-venv setup-analysis

install-deps:
	python -m pip install --upgrade pip virtualenv

install-deps-user:
	python -m pip install --user --upgrade pip virtualenv

clean:
	find . -iname __pycache__ | xargs rm -fr
	find . -iname '*.pyc' | xargs rm -f

clean-venv:
	rm -fr .venv

clean-pypi:
	rm -fr build dist *.egg-info

dist-clean: clean clean-venv clean-pypi

pypi-dist: clean-pypi
	python setup.py bdist_wheel --universal

update-coverage-requirements: setup-venv setup-coverage
	pip freeze > misc/.coverage-requirements.txt

update-analysis-requirements: setup-venv setup-analysis
	pip freeze > misc/.analysis-requirements.txt

check-style:
	flake8 --count --show-source ${TOP_LEVEL_FILES}

static-analysis:
	vulture --min-confidence 70 --sort-by-size ${TOP_LEVEL_FILES}

check-unused:
	vulture --sort-by-size ${VERMIN_FILES}

security-check:
	bandit -r -s B101 ${MODULES}

lint:
	pylint -j 0 --disable=C,W0201,W0311,W0621,W0703,W0707,R0801,R0902,R0903,R0904,R0911,R0913,R0914,R0915,R0916,R1702,R1725,E0611,E1136\
		${TOP_LEVEL_FILES}

check-pypi:
	pyroma --min=10 .

check: check-style check-pypi static-analysis lint

# NOTE: `check` doesn't check all because bandit doesn't run on py37+ yet.
check-all: check security-check

test-coverage:
	coverage run --source=vermin,tests runtests.py
	coverage run --append --source=vermin ./vermin.py -v -t=3 vermin.py vermin

coverage-report:
	coverage report -m
