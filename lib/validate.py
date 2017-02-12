'''
This file contains the functions that validate the
functions in the file lib/data.py

'''

import os
import data    #avoid using * while importing anything,as that can be ambigous,if two modules have same function 
                      #instead import particular function,delete the comment after reading
MIN_INT = -100000000000000000000
MAX_INT = 100000000000000000000
          
def valRandomInt(start = MIN_INT, end = MAX_INT):
    '''
    validates the input and output of randomInt() of data.py
    '''
    if start <= end and (start >= MIN_INT and end <= MAX_INT) and (end >= MIN_INT and end <= MAX_INT):
        output = randomInt(start, end)
        if output >= MIN_INT and output <= MAX_INT:
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
        output = data.randomAlpha(case)
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
    if (start >= 0 and start <= 255) and (end >= 0 and end <= 255) and (end >= start): #constraints check
        if range == True or range == False:                                            #range is enabled or not
            output = map(ord,data.randomAscii(start, end, range))
            if range == True:
                if min(output) >= 0 and max(output) <=255:
                    return True
                else:
                    return False
            else:
                if output >=0 and output <=255:
                    return True
                else:
                    return False

        else:
            return False
            


def valRandomInts(start = 0, end = 100, count = 100, unique = True):
    '''
    validates the input ,output of data.randomInts() 
    '''
    if end >= start and (start >=MIN_INT and start<= MAX_INT) and (start >=MIN_INT and start<= MAX_INT): 
        output = data.randomInts(start,end,unique=True)
        if min(output) >= MIN_INT and max(utput) <= MAX_INT:
            return True
        else:
            return False
    else:
        return True







