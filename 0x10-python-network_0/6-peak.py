#!/usr/bin/python3
"""find_peak module"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""
    l = len(list_of_integers)
    if l == 0:
        return None
    li = list_of_integers
    hi = l - 1
    lo = 0
    peak = li[0]
    while hi > lo:
        mid = int(lo + (hi - lo) / 2)
        if li[mid - 1] <= li[mid] >= li[mid + 1]:
            peak = li[mid]
            break
        if li[mid] <= li[mid + 1]:
            lo = mid + 1
        elif li[mid - 1] <= li[mid]:
            hi = mid - 1
    return peak
