#!/bin/bash
set -x

if [[ $TRAVIS_PYTHON_VERSION != 2.7 && $TRAVIS_PYTHON_VERSION != 3.4 ]]; then
  make coveralls
fi
