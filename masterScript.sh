#!/usr/bin/env bash

echo "linux-scalaiblity, threads: 2, 4, 8; object size: 8, 16, 32, 128"
./linux-scalabilityExtractor.py -t 8  -i 10   # didn't work on mole
./linux-scalabilityExtractor.py -s 8  -i 10
./linux-scalabilityExtractor.py -s 32 -i 10

echo "cache-scratch (passive-false sharing); threads: 2, 4, 8; object size: 4, 8, 16, 32, 64, 128"
./cache-scratchExtractor.py -t 8  -i 10
./cache-scratchExtractor.py -s 8  -i 10
./cache-scratchExtractor.py -s 16 -i 10
./cache-scratchExtractor.py -s 64 -i 10

echo "cache-thrash (active-false sharing); threads: 2, 4, 8; object size: 2, 4, 8, 16, 32"
./cache-thrashExtractor.py -t 2  -i 10
./cache-thrashExtractor.py -t 4  -i 10
./cache-thrashExtractor.py -t 8  -i 10
./cache-thrashExtractor.py -s 2  -i 10
./cache-thrashExtractor.py -s 4  -i 10
./cache-thrashExtractor.py -s 8  -i 10
./cache-thrashExtractor.py -s 16 -i 10
./cache-thrashExtractor.py -s 32 -i 10

echo "larson (server replicator); threads 2, 4, 8; object size: 8, 32, 128, 512, 2048"
./larsonExtractor.py -t 8 -i 10
./larsonExtractor.py -m 8   -M 8   -i 10
./larsonExtractor.py -m 32  -M 32  -i 10
./larsonExtractor.py -m 128 -M 128 -i 10

echo "threadtest; threads 2, 4, 8; object size: 8, 32"
./threadtestExtractor.py -t 4  -i 10
./threadtestExtractor.py -s 8  -i 10
./threadtestExtractor.py -s 32 -i 10

