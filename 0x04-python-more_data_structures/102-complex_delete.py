#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    pop_keys = []
    for key, val in a_dictionary.items():
        if val == value:
            pop_keys.append(key)
    for key in pop_keys:
        a_dictionary.pop(key)
    return a_dictionary
