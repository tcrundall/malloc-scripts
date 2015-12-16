#!/usr/bin/env bash
benchmark=$1

./statsGatherer.sh glib.log $1
./statsGatherer.sh tcmalloc.log $1 ~/src/gperftools/build/.libs/libtcmalloc.so
./statsGatherer.sh hoard.log $1 ~/src/Hoard/src/libhoard.so

echo glib
./extractor.py -f glib.log
echo tcmalloc
./extractor.py -f tcmalloc.log
echo hoard
./extractor.py -f hoard.log
