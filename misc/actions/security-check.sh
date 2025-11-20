#!/bin/bash
set -x

setup() {
  make install-deps setup-venv
  source .venv/bin/activate
  make setup-analysis
}

# Even if .venv is found, make sure required executables are found, otherwise setup anyway.
if [[ ! -d .venv ]] || [[ ! -f .venv/bin/bandit ]]; then
  setup
else
  source .venv/bin/activate
fi

make security-check
