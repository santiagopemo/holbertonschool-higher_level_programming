#!/usr/bin/python3
"""Number Of Lines Module"""


def number_of_lines(filename=""):
    """Function that returns the number of lines of a text file"""
    with open(filename, encoding="utf-8") as f:
        lines = 0
        for i in f:
            lines += 1
        return lines
