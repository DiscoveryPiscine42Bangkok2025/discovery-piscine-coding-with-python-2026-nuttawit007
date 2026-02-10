#!/usr/bin/env python3

import sys

count_argv = len(sys.argv) - 1
if count_argv == 0:
    print("none")
else:
    print(sys.argv[1])