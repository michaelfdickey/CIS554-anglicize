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

    Paramter: the intereger to anglicize
    Precondition: n is an integer in the range 0 <= n < 1,000,000

    """

    number_string = ''

    def anglicize0to9(n):
        """
        returns the neglish equivalent of single digit integer 0-9
        """
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

    def anglicize10to19(n):
        if n == 10:
            return 'ten'
        if n == 11:
            return 'eleven'
        if n == 12:
            return 'twelve'
        if n == 13:
            return 'thirteen'
        if n == 14:
            return 'fourteen'
        if n == 15:
            return 'fifteen'
        if n == 16:
            return 'sixteen'
        if n == 17:
            return 'seventeen'
        if n == 18:
            return 'eighteen'
        if n == 19: 
            return 'nineteen'

    def anglicize20to99(n):
        if n // 10 == 2:
            if n % 10 > 0:
                return 'twenty ' + anglicize0to9(n % 10)
            else:
                return 'twenty'

        if n // 10 == 3:
            if n % 10 > 0:
                return 'thirty ' + anglicize0to9(n % 10)
            else:
                return 'thirty'
        
        if n // 10 == 4:
            if n % 10 > 0:
                return 'forty ' + anglicize0to9(n % 10)
            else:
                return 'forty'
        
        if n // 10 == 5:
            if n % 10 > 0:
                return 'fifty ' + anglicize0to9(n % 10)
            else:
                return 'fifty'
        
        if n // 10 == 6:
            if n % 10 > 0:
                return 'sixty ' + anglicize0to9(n % 10)
            else:
                return 'sixty'
        
        if n // 10 == 7:
            if n % 10 > 0:
                return 'seventy ' + anglicize0to9(n % 10)
            else:
                return 'seventy'

        if n // 10 == 8:
            if n % 10 > 0:
                return 'eighty ' + anglicize0to9(n % 10)
            else:
                return 'eighty'

        if n // 10 == 9:
            if n % 10 > 0:
                return 'ninety ' + anglicize0to9(n % 10)
            else:
                return 'ninety'


        




    # call the appropriate sub function(s)
    if n < 10:
        number_string = anglicize0to9(n)
        return number_string

    if n >= 10 and n < 20:
        number_string = anglicize10to19(n)
        return number_string

    if n >= 20 and n < 100:
        number_string = anglicize20to99(n)
        return number_string
    


#dev test cases
n = random.randint(0,9)
print('n is: ', n)
print(anglicize(n))

n = random.randint(10,19)
print('n is: ', n)
print(anglicize(n))

n = random.randint(20,99)
print('n is: ', n)
print(anglicize(n))