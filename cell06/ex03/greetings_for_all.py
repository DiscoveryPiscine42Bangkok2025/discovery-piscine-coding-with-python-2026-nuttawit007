#!/usr/bin/env python3

def greetings(name=None):
    if type(name) == str:
        print(f"Hello {name}")
    elif type(name) == int:
        print("Error! It was not a name.")
    else:
        print("Hello, noble stranger.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)