#!/usr/bin/env bash

# Runs linux-scalability.sh script with a given object size iterating through
#  8 thread counts and all 3 implementations of malloc
# The results are stored in temp{x}.txt files where x is the number of
#  threads used for that benchmark

objSize=$1
rm results/temp*.txt
for i in {1..8}; do
  echo $i
  touch results/temp${i}.txt 
  for j in {1..3}; do
    ./linux-scalability.sh $i $objSize $j >> results/temp${i}.txt
  done
done
