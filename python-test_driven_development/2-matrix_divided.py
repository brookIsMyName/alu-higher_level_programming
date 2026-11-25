#!/usr/bin/python3
"""Divide each element of a rectangular numeric matrix."""


def matrix_divided(matrix, div):
    """Return a new matrix with each quotient rounded to two places."""
    if not isinstance(matrix, list) or any(
        not isinstance(row, list)
        or any(not isinstance(value, (int, float)) for value in row)
        for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if matrix and any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(value / div, 2) for value in row] for row in matrix]
