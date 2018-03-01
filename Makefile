self-test:
	./minpy.py -vv minpy.py

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
          --show-source *.py

static-analysis:
	vulture --min-confidence 70 --sort-by-size *.py

check: check-style static-analysis
