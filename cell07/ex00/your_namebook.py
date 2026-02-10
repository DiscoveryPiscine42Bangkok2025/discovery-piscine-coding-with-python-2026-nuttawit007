#!/usr/bin/env python3

def array_of_names(persons):
    names = []
    for first_name in persons.keys():
        names.append(first_name)
    return names


persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))