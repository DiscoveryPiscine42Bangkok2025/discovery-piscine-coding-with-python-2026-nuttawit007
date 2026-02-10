#!/usr/bin/env python3

arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = []
for num in arr:
    if num > 5:
        new_arr.append(num+2)

print(f"{arr}\n{new_arr}")