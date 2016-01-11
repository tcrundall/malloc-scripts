#!/usr/bin/env bash

# Runs cache-scratch.sh with a given thread count iterating through
#  4 object sizes and all 3 implementations of malloc
# The results are stored in temp{x}.txt files where x is the object size used
#  for that benchmark


nthreads=$1

rm results/temp*.txt
for i in 2 4 8 16 30 32 64 128; do
  echo "$i"

  touch results/temp${i}.txt 
  for j in {1..3}; do
    ./cache-scratch.sh $nthreads $i $j >> results/temp${i}.txt
  done
done
