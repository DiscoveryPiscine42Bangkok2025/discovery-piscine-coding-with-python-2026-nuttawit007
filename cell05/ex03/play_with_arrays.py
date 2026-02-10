#!/usr/bin/env python3

arr = [2, 8, 9, 48, 8, 22, -12, 2]
set_arr = set()
for num in arr:
    if num > 5:
        set_arr.add(num+2)

print(f"{arr}\n{set_arr}")