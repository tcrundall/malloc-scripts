#!/usr/bin/env python3
import re
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--threads', dest='threads', help='number of threads')
parser.add_argument('-i', '--iterations', dest='iterations', help='number of iterations')

args = parser.parse_args()


for i in [2, 8, 16, 64, 256, 1024]:
  print("Running with " + str(i) + " byte objects\n")
  with open("results/temp" + str(i) + ".txt", 'w') as writeFile:
    for j in range(0, 5):
      subprocess.call(['./larson.py', '-t', str(args.threads), '-m', str(i - 1),
                                      '-M', str(i),
                                      '-v', str(j),            '-i', str(args.iterations)])
      with open("results/temp.txt", 'r') as tempFile:
        line = tempFile.readline()
        writeFile.write(line)
