#!/usr/bin/python3
"""find_peak module"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""
    if len(list_of_integers) == 0:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
