#!/usr/bin/env bash

nthreads=$1

rm results/temp*.txt
for i in 2 4 8 16 32; do
  echo "$i"

  touch results/temp${i}.txt 
  for j in {1..3}; do
    ./cache-thrash.sh $nthreads $i $j >> results/temp${i}.txt
  done
done
