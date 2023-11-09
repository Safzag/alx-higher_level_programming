#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrating how to return a list with all values multiplied by a number
# without using any loops
#
# (C) 2023 zghari safae, Sale, Morocco
# email safaezghari100@gmail.com
# -----------------------------------------------------------


def weight_average(my_list=[]):
    if not my_list:
        return 0
    average = 0
    div = 0
    for tup in my_list:
        average += tup[0] * tup[1]
        div += tup[1]
    return float(average / div)
