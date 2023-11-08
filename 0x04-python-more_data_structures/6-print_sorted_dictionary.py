#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrating how to return the number of keys in a dictionary
#
# (C) 2023 safae zghari , Sale , Morocco
# email safaezghari100@gmail.com
# -----------------------------------------------------------


def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary):
        print("{:s}: {}".format(key, a_dictionary[key]))
