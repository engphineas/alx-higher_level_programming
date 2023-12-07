#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[entry ** 2 for entry in row] for row in matrix]
    return new_matrix
