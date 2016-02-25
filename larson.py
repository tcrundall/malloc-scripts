#!/usr/bin/env python3
import re
import argparse
import subprocess
import os
import statistics

matcher = re.compile("Throughput = ([0-9]+) operations per second.")

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--threads', dest='threads', help='number of threads')
parser.add_argument('-m', '--minSize', dest='minSize', help='size of objects')
parser.add_argument('-M', '--maxSize', dest='maxSize', help='size of objects')
parser.add_argument('-v', '--vers', dest='version', help='malloc implementation')
parser.add_argument('-i', '--iterations', dest='iterations', help='number of iterations')

args = parser.parse_args()

versionList = ["", "HOARD_PATH", "TCMALLOC_PATH", "EDIT_TCMALLOC_PATH", "SCALLOC_PATH"]

benchmark = "BENCHMARK_PATH/larson/larson"

env = os.environ.copy()
env['LD_PRELOAD'] = versionList[int(args.version)]

with open("results/temp.txt", 'w') as tempFile:
  for i in range(0,int(args.iterations)):
    subprocess.call([benchmark,  
                         '4', args.minSize, args.maxSize,
                         '1000', '1000000',
                         '1', args.threads], 
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
