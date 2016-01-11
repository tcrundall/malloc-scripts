#!/usr/bin/env bash

# Runs larson.sh with a given thread count iterating through
#  4 object sizes and all 3 implementations of malloc
# The results are stored in temp{x}.txt files where x is the object size used
#  for that benchmark

nthreads=$1

rm results/temp*.txt
for i in 8 32 128 512 2048; do
  echo "$i"
  touch results/temp${i}.txt 
  for j in {1..3}; do
    ./larson.sh $nthreads $i $i $j >> results/temp${i}.txt
  done
done
