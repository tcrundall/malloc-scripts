#!/usr/bin/env python3
import re

matcher = re.compile("Time elapsed = ([0-9]+\.[0-9]+) seconds.")


with open("results/cache-scratchResults.txt", 'w') as compilingFile:
	compilingFile.write("Thread count \t glib \t hoard \t tcmalloc\n")
	for i in range(1,9):
		resultString = str(i) + ""
		with open("results/temp" + str(i) + ".txt") as resultFile:
			for line in resultFile:
				timeElapsed = matcher.match(line)
				if timeElapsed:
					resultString = resultString + "\t" + str(float(timeElapsed.group(1)))
		compilingFile.write(resultString + "\n")			
