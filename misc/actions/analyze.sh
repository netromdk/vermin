#!/bin/bash
set -x

make setup-venv setup-analysis
source .venv/bin/activate
make check-all
