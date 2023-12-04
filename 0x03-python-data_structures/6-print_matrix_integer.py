#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for rows in range(len(matrix)):
            for entry in range(len(matrix[rows])):
                if entry != len(matrix[rows]) - 1:
                    spacing = ' '
                else:
                    spacing = ''
                print("{:d}".format(matrix[rows][entry]), end=spacing)
            print()
