#!/usr/bin/env python3
'''
    ?> ./parameters.py
    Number of parameters: 0.
    ?> ./parameters.py "initiation"
    Number of parameters: 1.
    ?> ./parameters.py "this" "is" "crazy" "there's" "everywhere!"
    Number of parameters: 5.
    ?>
'''
import sys
count_arg = len(sys.argv) - 1
print(f"Number of parameters: {count_arg}.")