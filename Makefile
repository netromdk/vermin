test: self-test
	python -c "import unittest; unittest.main('tests')"

self-test:
	./minpy.py minpy.py

count:
	python -c "from minpy import *; print('modules:', len(MOD_REQS)); print('members:', len(MOD_MEM_REQS)); print('kwargs:', len(KWARGS_REQS)); print('total:', len(MOD_REQS)+len(MOD_MEM_REQS)+len(KWARGS_REQS))"
