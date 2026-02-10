#!/usr/bin/env python3
'''
    ?> ./aff_rev_params.py | cat -e
    none$
    ?> ./aff_rev_params.py "coucou" | cat -e
    none$
    ?> ./aff_rev_params.py "Python" "piscine" "hello" | cat -e
    hello$
    piscine$
    Python$
    ?>
'''
import sys

count_arg = len(sys.argv) - 1
if count_arg < 2:
    print("none")
else:
    for i in range(count_arg, 0, -1):
        print(sys.argv[i])