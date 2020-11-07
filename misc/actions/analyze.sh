#!/bin/bash
set -x

if [[ ! -d .venv ]]; then
  make install-deps setup-venv setup-analysis
fi

source .venv/bin/activate
make check-all
