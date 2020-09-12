#!/bin/bash

if [[ $TRAVIS_PYTHON_VERSION != 2.7 && $TRAVIS_PYTHON_VERSION != 3.2 && $TRAVIS_PYTHON_VERSION != 3.3 && $TRAVIS_PYTHON_VERSION != 3.4 ]]; then
  make setup-venv
  if [[ $TRAVIS_PYTHON_VERSION = 3.5 ]]; then
    make setup-coverage-3.5
  else
    make setup-coverage
  fi
  make test-coverage
else
  make test;
fi

if [[ $TRAVIS_PYTHON_VERSION > 3.4 ]]; then
  if [[ $TRAVIS_PYTHON_VERSION = 3.5 ]]; then
    make setup-misc-3.5
  else
    make setup-misc
  fi
  source .venv/bin/activate
  make check
fi

if [[ $TRAVIS_PYTHON_VERSION > 3.4 ]]; then
  if [[ $TRAVIS_PYTHON_VERSION = 3.5 ]]; then
    make setup-bandit-3.5
  else
    make setup-bandit
  fi
  source .venv/bin/activate
  make security-check
fi
