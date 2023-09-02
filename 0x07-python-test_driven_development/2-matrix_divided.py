#!/usr/bin/python3
"""Module for matrix division function"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.
    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")

        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
