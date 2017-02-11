'''
This file contains the functions that validate the
functions in the file lib/data.py

'''

import os
from data import *

MAX_INT = 100000000000000000000
def valRandomInt(start = 0, end = 100):
    '''
    validates the input and output of randomInt() of data.py
    '''
    if start > 0 and start < MAX_INT and end > 0 and end < MAX_INT and start < MAX_INT:
        output = randomInt(start, end)
        if output > 0 and output < MAX_INT:
            return True
        else:
            return False
    else:
        return False


def valRandomAlpha (case = "lower"):
    '''
    validates the input and output of randomAlpha() of data.py
    '''
    if case == "lower" or case == "upper":
        output = randomAlpha(case)
        if case == "lower":
            if output >= 'a' and output <= 'z':
                return True
            else:
                return False
        if case == 'upper':
            if output >= 'A' and output <= 'z':
                return True
            else:
                return False
    else:
        return False


def valRandomAscii(start = 0, end = 255, range = True):
    '''
    validates the input and output of randomAscii() of data.py
    '''
    if start >= 0 and start <= 255 and end > 0 and end <= 255:
        if range == True or range == False:
            output = randomInts(start, end, range)
            if ord(output) >= 0 and ord(output) <= 255:
                return True
            else:
                return False
        else:
            return False
    else:
        return False



def valRandomInts(start = 0, end = 100, count = 100, unique = True):
    pass
