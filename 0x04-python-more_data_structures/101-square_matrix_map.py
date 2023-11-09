#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrating how to return a list with all values multiplied by a number
# without using any loops
#
# (C) 2023 zghari safae, Sale, Morocco
# email safaezghari100@gmail.com
# -----------------------------------------------------------


def square_matrix_map(matrix=[]):
    return list(map(lambda x: list(map(lambda i: i ** 2, x)), matrix))
