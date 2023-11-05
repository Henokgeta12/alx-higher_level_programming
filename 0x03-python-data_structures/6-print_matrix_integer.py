#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range(3):
        for y in range(3):
            print("{:d} ".format(matrix[x][y]), end="")
        print()
