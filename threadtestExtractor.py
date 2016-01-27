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

matcher = re.compile("Time elapsed = ([0-9]+\.[0-9]+)")

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--threads', dest='threads', help='number of threads')
parser.add_argument('-s', '--size', dest='size', help='size of objects')

args = parser.parse_args()

if args.threads is None:
	subprocess.call(['./threadtestStatsGathererThreads.sh', str(args.size)])
	with open("results/threadtest" + args.size + "size.txt", 'w') as compilingFile:
		compilingFile.write("Thread count \t glib \t hoard \t tcmalloc\n")
		for i in range(1,9):
			resultString = str(i) + ""
			with open("results/temp" + str(i) + ".txt") as resultFile:
				for line in resultFile:
					timeElapsed = matcher.match(line)
					if timeElapsed:
						resultString = resultString + "\t" + str(float(timeElapsed.group(1)))
			compilingFile.write(resultString + "\n")			


if args.size is None:
	subprocess.call(['./threadtestStatsGathererObjectSize.sh', str(args.threads)])
	with open("results/threadtest" + args.threads +"threads.txt", 'w') as compilingFile:
		compilingFile.write("ObjSize \t glib \t hoard \t tcmalloc\n")
		for i in [2, 4, 8, 16, 32]:
			resultString = str(i) + ""
			with open("results/temp" + str(i) + ".txt") as resultFile:
				for line in resultFile:
					timeElapsed = matcher.match(line)
					if timeElapsed:
						resultString = resultString + "\t" + str(float(timeElapsed.group(1)))
			compilingFile.write(resultString + "\n")			
