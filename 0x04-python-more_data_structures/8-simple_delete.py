#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrating how to return the number of keys in a dictionary
#
# (C) 2023 safae zghari , Sale , Morocco
# email safaezghari100@gmail.com
# -----------------------------------------------------------


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
