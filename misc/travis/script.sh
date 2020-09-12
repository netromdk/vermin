#!/bin/bash
set -x

if [[ $TRAVIS_PYTHON_VERSION = 2.7 || $TRAVIS_PYTHON_VERSION = 3.4 ]]; then
  make test
  exit 0
fi

if [[ $TRAVIS_PYTHON_VERSION = 3.5 ]]; then
  make setup-3.5
else
  make setup
fi

source .venv/bin/activate

make test-coverage
make check-all
