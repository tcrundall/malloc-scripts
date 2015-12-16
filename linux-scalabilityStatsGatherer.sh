#!/usr/bin/env bash

#thread count
rm results/temp*.txt
for i in {1..8}; do
  touch results/temp${i}.txt 
  for j in {1..3}; do
    ./linux-scalability.sh $i $j >> results/temp${i}.txt
  done
done
