#!/usr/bin/env python3
import re
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--size', dest='size', help='size of objects')
parser.add_argument('-i', '--iterations', dest='iterations', help='number of iterations')

args = parser.parse_args()


for i in range(1, 9):
  with open("results/temp" + str(i) + ".txt", 'w') as writeFile:
    for j in range(0, 4):
      subprocess.call(['./linux-scalability.py',
               '-t', str(i), '-s', str(args.size),
               '-v', str(j), '-i', str(args.iterations)])
      with open("results/temp.txt", 'r') as tempFile:
        line = tempFile.readline()
        #print("read line is: " + line)
        writeFile.write(line)
