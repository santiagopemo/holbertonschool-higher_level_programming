#!/usr/bin/python3
"""Read Lines Module"""


def read_lines(filename="", nb_lines=0):
    """Function that reads n lines of a text file and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        lines = 1
        for l in f:
            print(l, end="")
            if lines == nb_lines:
                break
            lines += 1
