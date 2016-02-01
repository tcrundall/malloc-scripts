#!/usr/bin/env python
import re
import argparse

from pylab import *
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--benchmark', dest='benchmark', help='name of desired benchmark')
parser.add_argument('-t', '--threads',   dest='threads',   help='number of threads')
parser.add_argument('-s', '--size',      dest='size',      help='size of objects')

args = parser.parse_args()

# INSERT IF STATEMENTS HERE!!!!
successful = False
benchMachine = "torrey"
if args.threads is None:
  fileName = 'results/'+str(args.benchmark)+str(args.size)+'size.txt'
  imageName =  str(args.benchmark)+benchMachine.capitalize()+str(args.size)+'size'
  plt.xlabel('thread count')
  plt.title(str(args.benchmark).capitalize()+' on '+benchMachine.capitalize()+\
            ' Architecture with Object Size '+str(args.size))

if args.size is None:
  fileName = 'results/'+str(args.benchmark)+str(args.threads)+'threads.txt'
  imageName =  str(args.benchmark)+benchMachine.capitalize()+str(args.threads)+'threads'
  plt.xlabel('object size (bytes)')
  plt.semilogx(basex=2)
  plt.title(str(args.benchmark).capitalize()+' on '+benchMachine.capitalize()+\
           ' Architecture with Thread Count '+str(args.threads))

try:
# looking for txt file
  with open(fileName, 'r') as f:
    header = f.readline().strip().replace(' ','').upper().split('\t')
    array = []
    for i in range(len(header)):
      array.append([])
    for line in f:
      data = line.strip().split('\t')
      for i in range(len(data)):
        array[i].append(float(data[i]))

  if (args.benchmark == "larson"):
    plt.ylabel('Throughput')
  else:
    plt.ylabel('time (s)')

  plt.errorbar(array[0], array[1], yerr=array[2], fmt='--ro', label='glib')     # mean times of glib
  plt.errorbar(array[0], array[3], yerr=array[4], fmt='--yo', label='Hoard')    # mean times of hoard
  plt.errorbar(array[0], array[5], yerr=array[6], fmt='--bo', label='TCMalloc') # mean times of tcmalloc
  plt.errorbar(array[0], array[7], yerr=array[8], fmt='--mo', label='edited-TCM') # mean times of tcmalloc-edited
  plt.errorbar(array[0], array[9], yerr=array[10], fmt='--go', label='scalloc') # mean times of scalloc
  
  plt.legend(loc=2) 
  plt.loc = 2
  minimumy = min(array[1] + array[3] + array[5] + array[7] + array [9] + [0])
  maximumy = max(array[1] + array[3] + array[5] + array[7] + array [9]) #data point
  maximumy = maximumy * 1.6  #leaves space for legend/error bars
  plt.axis([min(array[0]), max(array[0]), minimumy, maximumy]) 
  plt.savefig('plots/' + imageName)
except IOError:
  print "Failed: "+fileName
  pass
