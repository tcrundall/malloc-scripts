#!/usr/bin/env bash

HOARD_PATH="$(find ~ -name "libhoard.so")"
TCMALLOC_PATH="$(find ~ -path *gperftools/build/.libs/libtcmalloc.so)"
EDIT_TCMALLOC_PATH="$(find ~ -path *gperftools-edited/build/.libs/libtcmalloc.so)"
SCALLOC_PATH="$(find ~ -path *lib.target/libscalloc.so)"
BENCHMARK_PATH="$(find ~ -name "Hoard")"

count=0
rm config.txt
touch config.txt
if [ -n "$HOARD_PATH" ]
   then
      let "count += 1"
      echo $HOARD_PATH  >> config.txt
fi

if [ -n "$TCMALLOC_PATH" ]
   then
      let "count += 1"
      echo $TCMALLOC_PATH >> config.txt
fi

if [ -n "$EDIT_TCMALLOC_PATH" ]
   then
      let "count += 1"
      echo $EDIT_TCMALLOC_PATH >> config.txt
fi

if [ -n "$SCALLOC_PATH" ]
   then
      let "count += 1"
      echo $SCALLOC_PATH >> config.txt
fi

if [ -n "$BENCHMARK_PATH" ]
   then
      let "count += 1"
      echo $BENCHMARK_PATH >> config.txt
fi
#echo "${count}"
#echo "${HOARD_PATH}"
#echo "${SCALLOC_PATH}"
#perl -i -p -e "'s/sup/$HOARD_PATH/g;' funsies.txt"
