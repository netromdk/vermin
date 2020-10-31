#!/bin/bash
set -x

PYTHON_VERSION=$(python -c "import sys;v=sys.version_info;print('{}.{}'.format(v[0],v[1]))")

if [[ $PYTHON_VERSION = 2.7 || $PYTHON_VERSION = 3.4 || $PYTHON_VERSION = 3.5 ]]; then
  make test
  exit 0
fi

make setup-venv setup-coverage
source .venv/bin/activate
make test-coverage
make coveralls
