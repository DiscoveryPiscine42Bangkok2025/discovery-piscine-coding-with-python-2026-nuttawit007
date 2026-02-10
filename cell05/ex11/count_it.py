#!/usr/bin/env python3
'''
    ?> ./count_it.py | cat -e
    none$
    ?> ./count_it.py "Game" "of" "Thrones" | cat -e
    parameters: 3$
    Game: 4$
    of: 2$
    Thrones: 7$
'''
import sys

count_param = len(sys.argv) - 1
if count_param == 0:
    print("none")
else:
    print(f'parameters: {count_param} ')
    for i in range(1, len(sys.argv)):
        print(f'{sys.argv[i]}: {len(sys.argv[i])}')