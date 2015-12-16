#!/usr/bin/env bash

objSize=$1
rm results/temp*.txt
for i in {1..8}; do
  echo $i
  touch results/temp${i}.txt 
  for j in {1..3}; do
    ./cache-thrash.sh $i $objSize $j >> results/temp${i}.txt
  done
done
