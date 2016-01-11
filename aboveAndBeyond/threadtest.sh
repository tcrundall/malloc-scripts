#!/usr/bin/env bash

# Runs threadtest benchmark with parameters:
#    nthreads objectSize malloc version [1 = glib, 2 = hoard, 3 = tcmalloc]

nthreads=$1
objectSize=$2
mallocVers=$3

if [[ $mallocVers = 2 ]]; then
  LD_PRELOAD=~/src/Hoard/src/libhoard.so ~/src/Hoard/benchmarks/threadtest/threadtest $nthreads 50 30000 10 $objectSize
elif [[ $mallocVers = 3 ]]; then
  LD_PRELOAD=~/src/gperftools/build/.libs/libtcmalloc.so ~/src/Hoard/benchmarks/threadtest/threadtest $nthreads 50 30000 10 $objectSize
else
  ~/src/Hoard/benchmarks/threadtest/threadtest $nthreads 50 30000 10 $objectSize 
fi

