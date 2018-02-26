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
