#! /usr/bin/env python3

num = input("Give me a number: ")
try:
    int_num = int(num)
    print("This number is an integer.")
except ValueError:
    print("This number is a float.")