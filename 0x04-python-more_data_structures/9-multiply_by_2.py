#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrating how to return the number of keys in a dictionary
#
# (C) 2023 safae zghari , Sale , Morocco
# email safaezghari100@gmail.com
# -----------------------------------------------------------


def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for key, value in new_dict.items():
        new_dict[key] = value * 2
    return new_dict
