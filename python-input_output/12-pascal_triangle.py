#!/usr/bin/python3
"""Provide a function for constructing Pascal's triangle."""


def pascal_triangle(n):
    """Return the first n rows of Pascal's triangle, or an empty list."""
    triangle = []
    for index in range(n):
        row = [1] * (index + 1)
        for column in range(1, index):
            previous = triangle[index - 1]
            row[column] = previous[column - 1] + previous[column]
        triangle.append(row)
    return triangle
