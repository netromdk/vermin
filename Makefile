test: self-test
	python -c "import unittest; unittest.main('lang_tests')"
	python -c "import unittest; unittest.main('module_tests')"
	python -c "import unittest; unittest.main('class_tests')"
	python -c "import unittest; unittest.main('function_tests')"
	python -c "import unittest; unittest.main('constants_tests')"
	python -c "import unittest; unittest.main('kwargs_tests')"

self-test:
	./minpy.py minpy.py

count:
	python -c "from minpy import *; print('modules:', len(MOD_REQS)); print('members:', len(MOD_MEM_REQS)); print('kwargs:', len(KWARGS_REQS)); print('total:', len(MOD_REQS)+len(MOD_MEM_REQS)+len(KWARGS_REQS))"

setup: clean
	virtualenv -p python .venv
	.venv/bin/pip install -r .misc-requirements.txt

clean:
	rm -fr .venv
	find . -iname __pycache__ | xargs rm -fr

update-requirements: setup
	.venv/bin/pip freeze > .misc-requirements.txt

check-style:
	flake8 --ignore E111,E114,E121,E126,E127,E302,E305 --max-line-length 100 --count \
          --show-source *.py

static-analysis:
	vulture --min-confidence 70 --sort-by-size *.py

check: check-style static-analysis
