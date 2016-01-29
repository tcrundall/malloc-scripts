#!/usr/bin/env bash

# Runs linux-scalability benchmark with parameters:
#    nthreads objectSize malloc version [1 = glib, 2 = hoard, 3 = tcmalloc]


nthreads=$1
objectSize=$2
mallocVers=$3

if [[ $mallocVers = 2 ]]; then
  LD_PRELOAD=~/src/Hoard/src/libhoard.so ~/src/Hoard/benchmarks/linux-scalability/linux-scalability $objectSize  1000000 $nthreads
elif [[ $mallocVers = 3 ]]; then
  LD_PRELOAD=~/src/gperftools/build/.libs/libtcmalloc.so ~/src/Hoard/benchmarks/linux-scalability/linux-scalability $objectSize 1000000 $nthreads
else
  ~/src/Hoard/benchmarks/linux-scalability/linux-scalability $objectSize 1000000 $nthreads
fi

