MINPY_FILES=minpy.py `find minpy -iname '*.py'`
TEST_FILES=runtests.py `find tests -iname '*.py'`

self-test:
	./minpy.py -v ${MINPY_FILES}

test: self-test
	./runtests.py

test-all:
	python2.7 ./runtests.py
	python3.2 ./runtests.py
	python3 ./runtests.py

count:
	./count.py

setup: clean
	virtualenv -p python .venv
	.venv/bin/pip install -r .misc-requirements.txt

clean:
	rm -fr .venv
	find . -iname __pycache__ | xargs rm -fr
	find . -iname '*.pyc' | xargs rm -f

update-requirements: setup
	.venv/bin/pip freeze > .misc-requirements.txt

check-style:
	flake8 --ignore E111,E114,E121,E126,E127,E302,E305 --max-line-length 100 --count \
          --show-source ${MINPY_FILES} ${TEST_FILES}

static-analysis:
	vulture --min-confidence 70 --sort-by-size ${MINPY_FILES} ${TEST_FILES}

check: check-style static-analysis
