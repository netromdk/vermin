#!/bin/sh
# Profile code triggered via input files but only with one process to simplify results for human
# parsing.

PROF_FILE=/tmp/out.prof
FLD=$(dirname $0)
VERMIN=${FLD}/vermin.py

if [ $# -eq 0 ]; then
  echo "usage: $0 <files to analyze with Vermin>"
  exit 1
fi

if ! hash pyprof2calltree 2>/dev/null; then
  echo "Required program not found: pyprof2calltree"
  echo "$ pip3 install pyprof2calltree && rehash"
  exit 1
fi

set -x
time python3 -m cProfile -o "${PROF_FILE}" "${VERMIN}" -q -p=1 $@ && \
  pyprof2calltree -k -i "${PROF_FILE}"
