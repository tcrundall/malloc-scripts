#!/usr/bin/env bash

# to be performed in home folder (/home/tcrundall/)
mkdir src
cd src
# my edited TCMalloc
git clone https://github.com/tcrundall/gperftools.git
mv gperftools gperftools-edited
cd gperftools-edited
./autogen.sh
mkdir build
cd build
../configure
make -j12
cd ../..

git clone https://github.com/gperftools/gperftools.git
cd gperftools
./autogen.sh
mkdir build
cd build
../configure
make -j12
cd ../..

git clone --recursive https://github.com/emeryberger/Hoard.git
cd Hoard
cd src
make Linux-gcc-x86_64
cd ../benchmarks
make
cd ../..

git clone https://github.com/cksystemsgroup/scalloc.git
cd scalloc
tools/make_deps.sh
build/gyp/gyp --depth=. scalloc.gyp
V=1 BUILDTYPE=Release make
cp out/Release/lib.target/libscalloc.so out/libscalloc-x86_64.so
# sudo sh -c "echo 1 > /proc/sys/vm/overcommit_memory"
cd ..

git clone https://github.com/tcrundall/malloc-scripts.git
