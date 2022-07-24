#!/bin/bash
set -x

PYTHON_VERSION=$(python -c "import sys;v=sys.version_info;print('{}.{}'.format(v[0],v[1]))")

if [[ $PYTHON_VERSION = 3.4 ||
      $PYTHON_VERSION = 3.5 ||
      $PYTHON_VERSION = 3.6 ]];
then
  make test
else
  setup() {
    make install-deps setup-venv
    source .venv/bin/activate
    make setup-coverage
  }

  # Even if .venv is found, make sure required executables are found, otherwise setup anyway.
  if [[ ! -d .venv ]] || [[ ! -f .venv/bin/coveralls ]]; then
    setup
  else
    source .venv/bin/activate
  fi

  make test-coverage

  # Output debug info to be able to troubleshoot in cases when the Coveralls command beneath fails.
  coveralls debug --service=github-actions

  # Note that it requires COVERALLS_REPO_TOKEN to be set!
  coveralls --service=github-actions
fi
