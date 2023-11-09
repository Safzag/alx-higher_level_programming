#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrating how to return a list with all values multiplied by a number
# without using any loops
#
# (C) 2023 zghari safae, Sale, Morocco
# email safaezghari100@gmail.com
# -----------------------------------------------------------


# Import the add function
from task import add

a = 1
b = 2

# This code should not run when this file is imported
if __name__ == "__main__":
    print("{:d} + {:d} = {:d}". format(a, b, add(a, b)))
