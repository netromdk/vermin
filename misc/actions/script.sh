#!/bin/bash
set -x

PYTHON_VERSION=$(python -c "import sys;v=sys.version_info;print('{}.{}'.format(v[0],v[1]))")

if [[ $PYTHON_VERSION = 2.7 || $PYTHON_VERSION = 3.4 ]]; then
  make test
  exit 0
fi

if [[ $PYTHON_VERSION = 3.5 ]]; then
  make setup-3.5
else
  make setup
fi

source .venv/bin/activate

make test-coverage
make check-all

# Don't push coverage from 3.5 because the build ID is wrong so it won't be attached the same as the
# other coverage results.
if [[ $PYTHON_VERSION != 3.5 ]]; then
  make coveralls
fi
