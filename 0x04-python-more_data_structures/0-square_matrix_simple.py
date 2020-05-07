#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [[col*col for col in row] for row in matrix]
    return new
