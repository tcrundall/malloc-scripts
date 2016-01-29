#!/usr/bin/env bash

echo "linux-scalaiblity, threads: 2, 4, 8; object size: 8, 16, 32, 128"
./linux-scalabilityExtractor.py -t 2   # didn't work on mole
./linux-scalabilityExtractor.py -t 4   # didn't work on mole
./linux-scalabilityExtractor.py -t 8   # didn't work on mole
./linux-scalabilityExtractor.py -s 8
./linux-scalabilityExtractor.py -s 16
./linux-scalabilityExtractor.py -s 32
./linux-scalabilityExtractor.py -s 128

echo "cache-scratch (passive-false sharing); threads: 2, 4, 8; object size: 4, 8, 16, 32, 64, 128"
./cache-scratchExtractor.py -t 2
./cache-scratchExtractor.py -t 4
./cache-scratchExtractor.py -t 8
./cache-scratchExtractor.py -s 4
./cache-scratchExtractor.py -s 8
./cache-scratchExtractor.py -s 16 
./cache-scratchExtractor.py -s 64 
./cache-scratchExtractor.py -s 128  

echo "cache-thrash (active-false sharing); threads: 2, 4, 8; object size: 2, 4, 8, 16, 32"
./cache-thrashExtractor.py -t 2
./cache-thrashExtractor.py -t 4
./cache-thrashExtractor.py -t 8
./cache-thrashExtractor.py -s 2
./cache-thrashExtractor.py -s 4
./cache-thrashExtractor.py -s 8
./cache-thrashExtractor.py -s 16
./cache-thrashExtractor.py -s 32

echo "larson (server replicator); threads 2, 4, 8; object size: 8, 32, 128, 512, 2048"
./larsonExtractor.py -t 2
./larsonExtractor.py -t 4
./larsonExtractor.py -t 8
./larsonExtractor.py -m 8 -M 8
./larsonExtractor.py -m 32 -M 32
./larsonExtractor.py -m 128 -M 128
./larsonExtractor.py -m 512 -M 512
./larsonExtractor.py -m 2048 -M 2048

echo "threadtest; threads 2, 4, 8; object size: 8, 32"
./threadtestExtractor.py -t 2
./threadtestExtractor.py -t 4
./threadtestExtractor.py -t 8
./threadtestExtractor.py -s 8
./threadtestExtractor.py -s 32
