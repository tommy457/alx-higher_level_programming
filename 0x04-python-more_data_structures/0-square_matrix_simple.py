#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix:
        new_matrix = matrix.copy()
        result = []
        for row in new_matrix:
            res = map(lambda x: x * x, row)
            result.append(list(res))
        return result
