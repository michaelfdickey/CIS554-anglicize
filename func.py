"""
Functions to anglicize integers in the range 1 -> 999,999

The primary function in this module is anglicize(). This is a great module to help understand preconditions

Author: Michael Dickey
Date: Dec 23, 2021
"""

import random 

def anglicize(n):
    """
    Returns: a string representation of the integer n in English

    Examples:
    3:      'three'
    45:     'forty five'
    100:    'one hundred'
    127:    'one hundred and twenty seven'
    1001:   'one thousand and one'
    990899: 'nine hundred and ninety eight thousand nine hundred and ninety nine'

    """
    if n < 10:
        if n == 0:
            return 'zero'
        if n == 1:
            return 'one'
        if n == 2:
            return 'two'
        if n == 3:
            return 'three'
        if n == 4:
            return 'four'
        if n == 5:
            return 'five'
        if n == 6:
            return 'six'
        if n == 7:
            return 'seven'
        if n == 8:
            return 'eight'
        if n == 9:
            return 'nine'







#dev test cases
n = random.randint(0,9)
print('n is: ', n)
print(anglicize(n))

