#! /usr/bin/env python3

print("Enter a number")
num = int(input())
for i in range(0, 10, 1):
    result = num * i
    print(f"{num} x {i} = {result}")