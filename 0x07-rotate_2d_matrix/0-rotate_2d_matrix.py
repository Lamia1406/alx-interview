#!/usr/bin/python3
"this module contains a function that rotatea a matrix 90deg"


def rotate_2d_matrix(matrix):
    "a function that rotates a matrix 90deg clockwise"
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row = row.reverse()
