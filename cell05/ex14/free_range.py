#!/usr/bin/env python3
import sys
'''
    ?> ./free_range.py | cat -e
    none$
    ?> ./free_range.py 10 14 | cat -e
    [10, 11, 12, 13, 14]$
    ?>
'''
count_param = len(sys.argv) - 1
if count_param != 2:
    print("none")
else:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    result = list(range(start, end + 1))
    print(result)