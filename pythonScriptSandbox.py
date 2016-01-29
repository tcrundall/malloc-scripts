#!/usr/bin/env python3
import sys
import subprocess


subprocess.Popen(["echo", "hello world"], stdout=subprocess.PIPE)

subprocess.call(['echo', 'sup']) 
subprocess.call('ls')
#subprocess.call(['cd', '..'])
subprocess.call(['./cache-thrash.sh'])
subprocess.call(['./oldScripts/cache-thrash.sh'])
subprocess.call(['/home/tcrundall/src/Hoard/benchmarks/cache-thrash/cache-thrash', '8', '20', '8', '1'])
subprocess.call('ls')
