#!/bin/bash
set -x

make setup-venv setup-misc setup-bandit
source .venv/bin/activate
make check-all
