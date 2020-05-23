#!/usr/bin/python3
"""
Add integer module
contains:
add_integer fucntion
"""


def add_integer(a, b=98):
    """
    Adds two integers
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return a + b
