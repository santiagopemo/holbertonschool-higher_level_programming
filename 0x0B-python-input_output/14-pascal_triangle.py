#!/usr/bin/python3
"""Pascal Triangle Module"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = []
        for j in range(i + 1):
            first_idx = j - 1
            second_idx = j
            if first_idx == -1:
                first = 0
            else:
                first = triangle[i - 1][first_idx]
            if second_idx == len(triangle[i - 1]):
                second = 0
            else:
                second = triangle[i - 1][second_idx]
            row.append(first + second)
        triangle.append(row)
    return triangle
