#!/usr/bin/env python3
import re
import argparse
import statistics
matcher = re.compile("Time elapsed = ([0-9]+\.[0-9]+)")
resultList = []

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', dest='log', help='File of results')

args = parser.parse_args()

if args.log is None:
	args.log = "results.log"

with open(args.log) as resultFile:
	for line in resultFile:
		timeElapsed = matcher.match(line)
		if timeElapsed:
			resultList.append(float(timeElapsed.group(1)))

print(statistics.mean(resultList))
print(statistics.stdev(resultList))
			
