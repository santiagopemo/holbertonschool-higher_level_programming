#!/usr/bin/python3
"""find_peak module"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""
    l = len(list_of_integers)
    if l == 0:
        return None
    peak = list_of_integers[0]
    for i in range(l):
        if i > 0:
            prev = list_of_integers[i - 1]
        else:
            prev = list_of_integers[i]
        if i == (l - 1):
            next = list_of_integers[i]
        else:
            next = list_of_integers[i + 1]
        v = list_of_integers[i]
        if prev <= v >= next:
            peak = v
    return peak
