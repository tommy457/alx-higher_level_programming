#!/usr/bin/python3
""""Module for pascal_triangle method"""


def pascal_triangle(n):
    """Method that returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    if n <= 0:
        return []

    elements = [[1]]
    while len(elements) != n:
        firstElem = elements[-1]
        tmp = [1]
        for i in range(len(firstElem) - 1):
            tmp.append(firstElem[i] + firstElem[i + 1])
        tmp.append(1)
        elements.append(tmp)
    return elements
