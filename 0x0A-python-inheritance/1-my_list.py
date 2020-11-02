#!/usr/bin/python3
"""My List Module"""


class MyList(list):
    """My List Class"""
    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
