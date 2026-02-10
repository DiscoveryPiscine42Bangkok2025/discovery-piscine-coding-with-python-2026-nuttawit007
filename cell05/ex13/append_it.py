#!/usr/bin/env python3
'''
    ?> ./append_it.py | cat -e
    none$
    ?> ./append_it.py "parallel" "egoism" "human" | cat -e
    parallelism$
    humanism$
'''
import sys

if len(sys.argv) < 2:
    print("none")
else:
    for arg in sys.argv[1:]:
        if arg.endswith("ism"):
            print(arg)
        else:
            print(arg + "ism")

