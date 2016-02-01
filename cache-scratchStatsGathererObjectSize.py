#!/usr/bin/env python3
import re
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--threads', dest='threads', help='number of threads')
parser.add_argument('-i', '--iterations', dest='iterations', help='number of iterations')

args = parser.parse_args()

print("Running cache-scratch with fixed " + str(args.threads) + " threads")
for i in [2, 4, 8, 16, 32, 64]:
  print("-- Running with " + str(i) + " byte objects")
  with open("results/temp" + str(i) + ".txt", 'w') as writeFile:
    for j in range(0, 5):
      subprocess.call(['./cache-scratch.py', '-t', str(args.threads), '-s', str(i),
                                             '-v', str(j),            '-i', str(args.iterations)])
      with open("results/temp.txt", 'r') as tempFile:
        line = tempFile.readline()
        writeFile.write(line)
