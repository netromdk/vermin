test: self-test
	python -c "import unittest; unittest.main('tests')"

self-test:
	./minpy.py minpy.py
