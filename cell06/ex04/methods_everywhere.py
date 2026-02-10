#!/usr/bin/env python3

import sys

def shrink(txt):
    print(txt[:8])
    
def enlarge(txt):
    print(txt.ljust(8, "Z"))
    
if len(sys.argv) > 1:
    for i in sys.argv[1:]:
        if len(i) > 8:
            shrink(i)
        elif len(i) < 8:
            enlarge(i)
        else:
            print(i)
else:
    print("none")