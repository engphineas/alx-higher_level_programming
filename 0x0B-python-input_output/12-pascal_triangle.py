#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Representation of Pascal's Triangle of size n.

    Returns a list of lists representing the triangle of integers.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        triangle1 = triangle[-1]
        temp = [1]
        for j in range(len(triangle1) - 1):
            temp.append(triangle1[j] + triangle[j + 1])
        temp.append(1)
        triangle.append(temp)
    return triangle
