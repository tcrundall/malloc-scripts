#!/usr/bin/env bash
#args: nthreads [malloc version: 1 = glib, 2 = hoard, 3 = tcmalloc]


nthreads=$1
mallocVers=$2

#mallocLib=""

if [[ $mallocVers = 2 ]]; then
  LD_PRELOAD=~/src/Hoard/src/libhoard.so ~/src/Hoard/benchmarks/linux-scalability/linux-scalability 8 10000000 $nthreads
  #mallocLib = "LD_PRELOAD=~/src/Hoard/src/libhoard.so"
elif [[ $mallocVers = 3 ]]; then
  LD_PRELOAD=~/src/gperftools/build/.libs/libtcmalloc.so ~/src/Hoard/benchmarks/linux-scalability/linux-scalability 8 10000000 $nthreads
#  $mallocLib = "LD_PRELOAD=~/src/gperftools/build/.libs/libtcmalloc.so"
else
  ~/src/Hoard/benchmarks/linux-scalability/linux-scalability 8 10000000 $nthreads 
fi

