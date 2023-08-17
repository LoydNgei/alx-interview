#!/usr/bin/python3
"""Given an n x n 2D matrix, rotate it 90 degrees clockwise"""


def transpose_matrix(matrix, n):
    """Transpose matrix in place"""
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_matrix(matrix):
    """Reverse matrix in place"""
    for row in matrix:
        row.reverse()


def rotate_2d_matrix(matrix):
    """Do the actual rotation"""
    n = len(matrix)

    transpose_matrix(matrix, n)
    reverse_matrix(matrix)

    return matrix
