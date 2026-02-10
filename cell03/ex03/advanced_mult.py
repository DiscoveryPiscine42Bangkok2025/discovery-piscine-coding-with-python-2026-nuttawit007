#! /usr/bin/env python3

import sys
if len(sys.argv) > 1:
    print("none")
    sys.exit(1)

num = 0
while num <= 10:
    print(f"Table de {num}: {num} {num*1} {num*2} {num*3} {num*4} {num*5} {num*6} {num*7} {num*8} {num*9} {num*10}")
    num += 1