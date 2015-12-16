#!/usr/bin/env bash
#args: outputFileName benchmarkExecutable [library]
export LD_PRELOAD=$3
benchmark=$2
logname=$1
rm $1
pushd ~/src/Hoard/benchmarks
for i in {1..30}; do
  $2 >> $1
done
popd
