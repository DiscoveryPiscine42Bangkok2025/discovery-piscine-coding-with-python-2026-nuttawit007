#!/usr/bin/env python3
import sys

count_arg = len(sys.argv) - 1
if count_arg == 0:
    print("none")
else:
    for i in range(1, len(sys.argv)): 
        print(sys.argv[i].lower())