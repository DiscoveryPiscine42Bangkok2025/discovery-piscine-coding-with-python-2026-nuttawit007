#!/usr/bin/env python3
'''
    ?> ./string_are_arrays.py | cat -e
    none$
    ?> ./string_are_arrays.py "The character Z is not found in this string" | cat -e
    none$
    ?> ./string_are_arrays.py "The character z is found in this string" | cat -e
    z$
    ?> ./string_are_arrays.py "Zaz visits the zoo with Zazie" | cat -e
    zzz$
    ?>
'''
import sys

count_arg = len(sys.argv) - 1
if count_arg != 1:
    print("none")
else:
    input_str = sys.argv[1]
    result = ''
    for char in input_str:
        if char == 'z':
            result += 'z'
    if result == '':
        print("none")
    else:
        print(result)