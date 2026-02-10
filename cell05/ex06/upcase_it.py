#!/usr/bin/env python3
''' 
    ?> ./upcase_it.py | cat -e
    none$
    ?> ./upcase_it.py "initiation" | cat -e
    INITIATION$
    ?> ./upcase_it.py 'This exercise is quite easy!' | cat -e
    THIS EXERCISE IS QUITE EASY!$
    ?>
'''

import sys

count_arg = len(sys.argv) - 1
if count_arg != 1:
    print("none")
else:
    print(sys.argv[1].upper())