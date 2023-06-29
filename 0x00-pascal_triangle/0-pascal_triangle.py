#!/usr/bin/python3
""" A function to create pascal triangle """


def pascal_triangle(n):
    if n <= 0:
        return []

    pascal = [[1]]

    for i in range(1, n):
        last_row = pascal[i - 1]
        this_row = [1]
        for j in range(1, i):
            this_row.append(last_row[j - 1] + last_row[j])
        this_row.append(1)
        pascal.append(this_row)

    return pascal
