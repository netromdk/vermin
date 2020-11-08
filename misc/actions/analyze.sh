#!/bin/bash
set -x

if [[ ! -d .venv ]]; then
  make install-deps setup-venv
  source .venv/bin/activate
  make setup-analysis
else
  source .venv/bin/activate
fi

make check-all
