#!/bin/bash
set -x

PYTHON_VERSION=$(python -c "import sys;v=sys.version_info;print('{}.{}'.format(v[0],v[1]))")

if [[ $PYTHON_VERSION = 2.7 || $PYTHON_VERSION = 3.4 || $PYTHON_VERSION = 3.5 ]]; then
  make test
  exit 0
fi

if [[ ! -d .venv ]]; then
  make install-deps setup-venv
  source .venv/bin/activate
  make setup-coverage
else
  source .venv/bin/activate
fi

make test-coverage

# Note that it requires COVERALLS_REPO_TOKEN to be set!
coveralls
