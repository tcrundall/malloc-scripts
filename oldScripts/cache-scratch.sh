#!/usr/bin/env bash


# Runs cache-scratch benchmark with parameters:
#    nthreads objectSize malloc version [1 = glib, 2 = hoard, 3 = tcmalloc]

nthreads=$1
objectSize=$2
mallocVers=$3

if [[ $mallocVers = 2 ]]; then
  LD_PRELOAD=~/src/Hoard/src/libhoard.so ~/src/Hoard/benchmarks/cache-scratch/cache-scratch $nthreads 100 $objectSize 1000000
elif [[ $mallocVers = 3 ]]; then
  LD_PRELOAD=~/src/gperftools/build/.libs/libtcmalloc.so ~/src/Hoard/benchmarks/cache-scratch/cache-scratch $nthreads 100 $objectSize 1000000
else
  ~/src/Hoard/benchmarks/cache-scratch/cache-scratch $nthreads 100 $objectSize 1000000 
fi

