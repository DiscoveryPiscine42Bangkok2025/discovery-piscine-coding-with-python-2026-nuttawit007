#! /usr/bin/env python3

text = input()
result_text = ""

for char in text:
    if char.islower():
        result_text += char.upper()
    elif char.isupper():
        result_text += char.lower()
    else:
        result_text += char
print(result_text)