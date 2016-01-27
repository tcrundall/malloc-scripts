#!/usr/bin/env python3
import re
import argparse
import subprocess

# Usage: -t [number of threads]
#        -m [min object size] -M [max object size]
# The given argument fixes the appropriate property to the given value
#  and the appropriate statsGatherer will be called
# This script will then use the temp*.txt files created and compile
#  results into a csv table titled with 
#     [benchmark][min objectsize]min[max objectsize]maxSize.txt
#                                   or  [benchmark][threadcount]thread.txt

matcher = re.compile("Throughput = ([0-9]+) operations per second.")

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--threads', dest='threads', help='number of threads')
parser.add_argument('-m', '--min', dest='min', help='minimum object size')
parser.add_argument('-M', '--max', dest='max', help='maximum object size')

args = parser.parse_args()

if args.threads is None:
	subprocess.call(['./larsonStatsGathererThreads.sh', str(args.min), str(args.max)])
	with open("results/larson" + args.min + "min" + args.max + "maxSize.txt", 'w') as compilingFile:
		compilingFile.write("Thread count \t glib \t hoard \t tcmalloc\n")
		for i in range(1,9):
			resultString = str(i) + ""
			with open("results/temp" + str(i) + ".txt") as resultFile:
				for line in resultFile:
					timeElapsed = matcher.match(line)
					if timeElapsed:
						resultString = resultString + "\t" + str(float(timeElapsed.group(1)))
			compilingFile.write(resultString + "\n")			


if args.max is None:
	subprocess.call(['./larsonStatsGathererObjectSize.sh', str(args.threads)])
	with open("results/larson" + args.threads +"threads.txt", 'w') as compilingFile:
		compilingFile.write("ObjSize \t glib \t hoard \t tcmalloc\n")
		for i in [8, 16, 32, 64, 128]:
			resultString = str(i) + ""
			with open("results/temp" + str(i) + ".txt") as resultFile:
				for line in resultFile:
					timeElapsed = matcher.match(line)
					if timeElapsed:
						resultString = resultString + "\t" + str(float(timeElapsed.group(1)))
			compilingFile.write(resultString + "\n")			
