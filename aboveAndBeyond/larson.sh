#!/usr/bin/env bash


# Runs larson benchmark with parameters:
#    nthreads objectSize malloc version [1 = glib, 2 = hoard, 3 = tcmalloc]

nthreads=$1
minObjectSize=$2
maxObjectSize=$3
mallocVers=$4

if [[ $mallocVers = 2 ]]; then
  LD_PRELOAD=~/src/Hoard/src/libhoard.so ~/src/Hoard/benchmarks/larson/larson 4 $minObjectSize $maxObjectSize 1000 10000 1 $nthreads
elif [[ $mallocVers = 3 ]]; then
  LD_PRELOAD=~/src/gperftools/build/.libs/libtcmalloc.so ~/src/Hoard/benchmarks/larson/larson 4 $minObjectSize $maxObjectSize 1000 10000 1 $nthreads
else
  ~/src/Hoard/benchmarks/larson/larson 4 $minObjectSize $maxObjectSize 1000 10000 1 $nthreads 
fi

