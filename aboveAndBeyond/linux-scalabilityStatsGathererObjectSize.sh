#!/usr/bin/env bash

# Runs linux-scalability.sh script with a given thread count iterating through
#  4 object sizes and all 3 implementations of malloc
# The results are stored in temp{x}.txt files where x is the object size used
#  for that benchmark

nthreads=$1

rm results/temp*.txt
for i in 8 16 32 128 256 512 1024 2048; do
  echo "$i"

  touch results/temp${i}.txt 
  for j in {1..3}; do
    ./linux-scalability.sh $nthreads $i $j >> results/temp${i}.txt
  done
done
