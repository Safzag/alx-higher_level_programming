#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrating how to return the number of keys in a dictionary
#
# (C) 2023 safae zghari , Sale , Morocco
# email safaezghari100@gmail.com
# -----------------------------------------------------------


def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        for i in a_dictionary:
            if i == key:
                a_dictionary[i] = value
    return a_dictionary
