#!/usr/bin/env python3
import re
import argparse
import subprocess
import os
import statistics

matcher = re.compile("Average execution time = ([0-9]+\.[0-9]+) seconds.")

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--threads', dest='threads', help='number of threads')
parser.add_argument('-s', '--size', dest='size', help='size of objects')
parser.add_argument('-v', '--vers', dest='version', help='malloc implementation')
parser.add_argument('-i', '--iterations', dest='iterations', help='number of iterations')

args = parser.parse_args()

versionList = ["", \
  "/home/tcrundall/src/Hoard/src/libhoard.so", \
  "/home/tcrundall/src/gperftools/build/.libs/libtcmalloc.so", \
  "/home/tcrundall/src/gperftools-edited/build/.libs/libtcmalloc.so", \
  "/home/tcrundall/src/scalloc/out/libscalloc-x86_64.so"]

benchmark = "/home/tcrundall/src/Hoard/benchmarks/linux-scalability/linux-scalability"

env = os.environ.copy()
env['LD_PRELOAD'] = versionList[int(args.version)]

with open("results/temp.txt", 'w') as tempFile:
  for i in range(0,int(args.iterations)):
    subprocess.call([benchmark,  
                         args.size,    '1000000',
                         args.threads],                       
                         stdout=tempFile, env=env)

results = []
with open("results/temp.txt", 'r') as tempFile:
  for line in tempFile:
    timeElapsed = matcher.match(line)
    if timeElapsed:
      results.append(float(timeElapsed.group(1)))

average = statistics.mean(results)
stdev = statistics.stdev(results)
with open("results/temp.txt", 'w') as tempFile:
  tempFile.write(str(average) + '\t' + str(stdev) + '\n')
