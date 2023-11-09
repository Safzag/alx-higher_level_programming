#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrating how to return a list with all values multiplied by a number
# without using any loops
#
# (C) 2023 zghari safae, Sale, Morocco
# email safaezghari100@gmail.com
# -----------------------------------------------------------


def multiply_list_map(my_list=[], number=0):
    return list(map(lambda i: number * i, my_list))
