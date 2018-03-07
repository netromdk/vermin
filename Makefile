VERMIN_FILES=vermin.py `find vermin -iname '*.py'`
TEST_FILES=runtests.py `find tests -iname '*.py'`
OTHER_FILES=count.py
ALL_FILES=${VERMIN_FILES} ${TEST_FILES} ${OTHER_FILES}

self-test:
	./vermin.py -v ${VERMIN_FILES}

test: self-test
	./runtests.py

test-all:
	python2.7 ./runtests.py
	python3.2 ./runtests.py
	python3 ./runtests.py

count:
	./count.py

setup-venv: clean-venv
	virtualenv -p python .venv

setup-misc: clean
	.venv/bin/pip install -r .misc-requirements.txt

setup-coverage: clean
	.venv/bin/pip install -r .coverage-requirements.txt

setup: setup-venv setup-misc setup-coverage

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

update-misc-requirements: setup-venv setup-misc
	.venv/bin/pip freeze > .misc-requirements.txt

update-coverage-requirements: setup-venv setup-coverage
	.venv/bin/pip freeze > .coverage-requirements.txt

check-style:
	flake8 --ignore E111,E114,E121,E126,E127,E302,E305 --max-line-length 100 --count \
          --show-source ${ALL_FILES}

static-analysis:
	vulture --min-confidence 70 --sort-by-size ${ALL_FILES}

check-unused:
	vulture --sort-by-size ${VERMIN_FILES}

check: check-style static-analysis

test-coverage:
	.venv/bin/coverage run --source=vermin,tests runtests.py
	.venv/bin/coverage run --append --source=vermin ./vermin.py -v ${VERMIN_FILES}

coveralls:
	COVERALLS_REPO_TOKEN=twBSHlgE5AMFEQNmUK04LDcN7SVth3lDV .venv/bin/coveralls
