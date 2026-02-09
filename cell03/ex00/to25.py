#! /usr/bin/env python3
print("Enter a number less than 25:")
num = input()
if int(num) > 25:
    print("Error")
else:
    for i in range(int(num), 26):
        print("Inside the loop, my variable is: " + str(i))
