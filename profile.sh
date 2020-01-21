#!/bin/sh
PROF_FILE=/tmp/out.prof
FLD=$(dirname $0)
VERMIN=${FLD}/vermin.py

if [ $# -eq 0 ]; then
  echo "usage: $0 <files to analyze with Vermin>"
  exit 1
fi

# The following:
#   for proc_res in pool.imap(process_individual, ((path, config) for path in paths)):
# Could be made non-threaded via:
#   for proc_res in [process_individual((path, config)) for path in paths]:
echo "== Remember to disable threading in processor.py first! =="

set -x
time python -m cProfile -o "${PROF_FILE}" "${VERMIN}" -q $@ && \
  pyprof2calltree -k -i "${PROF_FILE}"
