#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrating how to return the number of keys in a dictionary
#
# (C) 2023 safae zghari , Sale , Morocco
# email safaezghari100@gmail.com
# -----------------------------------------------------------


def best_score(a_dictionary):
    if not a_dictionary:
        return (None)

    return (max(a_dictionary, key=a_dictionary.get))
