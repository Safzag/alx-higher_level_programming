#!/usr/bin/python3
# -----------------------------------------------------------
# Python program that:
# demonstrating how to return a list with all values multiplied by a number
# without using any loops
#
# (C) 2023 zghari safae, Sale, Morocco
# email safaezghari100@gmail.com
# -----------------------------------------------------------


def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_n = 0
    for j in range(len(roman_string)):
        if j > 0 and roman_d[roman_string[j]] > roman_d[roman_string[j - 1]]:
            roman_n += roman_d[roman_string[j]] - 2 * \
                        roman_d[roman_string[j - 1]]
        else:
            roman_n += roman_d[roman_string[j]]
    return roman_n
