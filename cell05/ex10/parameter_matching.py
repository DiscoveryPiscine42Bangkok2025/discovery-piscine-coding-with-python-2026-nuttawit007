#!/usr/bin/env python3
'''
    ?> ./parameter_matching.py
    none
    ?> ./parameter_matching.py "Hello"
    What was the parameter? Bonjour
    Nope, sorry...
    ?> ./parameter_matching.py "Hello"
    What was the parameter? Hello
    Good job!
    ?>
'''

import sys

count_args = len(sys.argv) - 1
if count_args != 1:
    print("none")
else:
    param = input("What was the parameter? ")
    if param == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")