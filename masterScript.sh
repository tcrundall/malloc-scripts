#!/usr/bin/env bash

echo "linux-scalability, threads: 8; object size: 8, 32"
./linux-scalabilityExtractor.py -t 8  -i 10   # didn't work on mole
./linux-scalabilityExtractor.py -s 8  -i 10
./linux-scalabilityExtractor.py -s 32 -i 10

echo "cache-scratch (passive-false sharing); threads: 8; object size: 8, 16, 64"
./cache-scratchExtractor.py -t 8  -i 10
./cache-scratchExtractor.py -s 8  -i 10
./cache-scratchExtractor.py -s 16 -i 10
./cache-scratchExtractor.py -s 64 -i 10

echo "cache-thrash (active-false sharing); threads: 8; object size: 4, 8, 32"
./cache-thrashExtractor.py -t 8  -i 10
./cache-thrashExtractor.py -s 4  -i 10
./cache-thrashExtractor.py -s 8  -i 10
./cache-thrashExtractor.py -s 32 -i 10

echo "larson (server replicator); threads 8; object size: 8, 32, 128"
./larsonExtractor.py -t 8   -i 10
./larsonExtractor.py -s 8   -i 10
./larsonExtractor.py -s 32  -i 10
./larsonExtractor.py -s 128 -i 10

echo "threadtest; threads 8; object size: 8, 32"
./threadtestExtractor.py -t 8  -i 10
./threadtestExtractor.py -s 8  -i 10
./threadtestExtractor.py -s 32 -i 10

