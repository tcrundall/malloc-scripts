#!/usr/bin/env bash

# Runs cache-thrash.sh with a given object size iterating through
#  8 thread counts and all 3 implementations of malloc
# The results are stored in temp{x}.txt files where x is the number of
#  threads used for that benchmark

objSize=$1
iterations=$2
rm results/temp*_*.txt
for m in $(seq 1 $iterations); do
  echo $m
  for i in {1..8}; do
    echo $i
    touch results/temp${i}_${m}.txt 
    for j in {1..3}; do
      ./cache-thrash.sh $i $objSize $j >> results/temp${i}_${iterations}.txt
    done
  done
done
