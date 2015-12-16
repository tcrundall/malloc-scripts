#/usr/bin/env bash
#args: nthreads [malloc version: 1 = glib, 2 = hoard, 3 = tcmalloc]

set -x
nthreads="$1"
mallocVers="$2"


if [[ $mallocVers = 2 ]]; then
  export LD_PRELOAD=~/src/Hoard/src/libhoard.so
elif [[ $mallocVers = 3 ]]; then
  export LD_PRELOAD=~/src/gperftools/build/.libs/libtcmalloc.so
fi

~/src/Hoard/benchmarks/linux-scalability/linux-scalability 8 10000000 "$nthreads"

