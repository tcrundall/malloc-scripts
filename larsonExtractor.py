#!/usr/bin/env python3
import re
import argparse
import subprocess

# Usage: -t [number of threads]
#        -s [object size]
# The given argument fixes the appropriate property to the given value
#  and the appropriate statsGatherer will be called
# This script will then use the temp*.txt files created and compile
#  results into a csv table titled with [benchmark][objectsize]size.txt
#                                   or  [benchmark][threadcount]thread.txt

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--threads', dest='threads', help='number of threads')
parser.add_argument('-s', '--size', dest='size', help='size of objects')
parser.add_argument('-i', '--iterations', dest='iterations', help='number of iterations')

args = parser.parse_args()

if not (args.threads is None) and not (args.size is None):
  print("Usage: you may only set either threads or size")

if args.threads is None:
  subprocess.call(['./larsonStatsGathererThreads.py',
                         '-s', str(args.size),
                         '-i', str(args.iterations)])
  with open("results/larson" + args.size + "size.txt", 'w') as compilingFile:
    compilingFile.write("Thread count\tglib\tstdev\thoard\tstdev\t" + \
                        "tcmalloc\tstdev\ttcmalloc-edited\tstdev\tscalloc\tstdev\n")
    for i in range(1,9):
      resultString = str(i) + ""
      with open("results/temp" + str(i) + ".txt") as resultFile:
        for line in resultFile:
          results = (line.strip()).split('\t')
          print(results)
          resultString = resultString + '\t' + results[0] + '\t' + results[1]
      compilingFile.write(resultString + '\n')      


if args.size is None:
  subprocess.call(['./larsonStatsGathererObjectSize.py', 
                        '-t', str(args.threads),
                        '-i', str(args.iterations)])
  with open("results/larson" + args.threads + "threads.txt", 'w') as compilingFile:
    compilingFile.write("Thread count\tglib\tstdev\thoard\tstdev\t" + \
                        "tcmalloc\tstdev\ttcmalloc-edited\tstdev\tscalloc\tstdev\n")
    for i in [2, 8, 16, 64, 256, 1024]:
      resultString = str(i) + ""
      with open("results/temp" + str(i) + ".txt") as resultFile:

        for line in resultFile:
          results = (line.strip()).split('\t')
          print(results)
          resultString = resultString + '\t' + results[0] + '\t' + results[1]
      compilingFile.write(resultString + '\n')      

