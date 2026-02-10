#!/usr/bin/env python3
'''
    ?> ./downcase_it.py | cat -e
    none$
    ?> ./downcase_it.py "LUCIOLE" | cat -e
    luciole$
    ?> ./downcase_it.py 'This exercise is quite easy!' | cat -e
    this exercise is quite easy!$
    ?>
'''

import sys

count_arg = len(sys.argv) - 1
if count_arg != 1:
    print("none")
else:
    print(sys.argv[1].lower())