test: self-test
	python -c "import unittest; unittest.main('general_tests')"
	python -c "import unittest; unittest.main('lang_tests')"
	python -c "import unittest; unittest.main('module_tests')"
	python -c "import unittest; unittest.main('class_tests')"
	python -c "import unittest; unittest.main('function_tests')"
	python -c "import unittest; unittest.main('constants_tests')"
	python -c "import unittest; unittest.main('kwargs_tests')"

self-test:
	./minpy.py -vv minpy.py

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
