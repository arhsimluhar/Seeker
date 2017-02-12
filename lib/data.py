'''
This file contains the functions that generate
data, in different formats and provide that as stdin to files

'''

import os
import random


def randomInt(start = 0 ,end = 100):
	'''
	returns any random number between start-end (inclusive)
	'''
	return random.randint(start,end)


def randomAlpha(start = 97,end = 122, case = "lower"):
	''' 	
	returns any random Alphabet between A-Z or a-z (inclusive)
	if case not specified give lowercase letter
	'''
	if case == "lower":
		return chr(randomInt(start,end))

	else:
		start = 65
		end = 90
		return chr(randomInt(start,end))



def randomAscii(start = 0,end = 255,range = True):
	'''
	returns any random ASCII character (0-255) (inclusive)
	'''
	if not range:
		return chr(randomInt(start,end))
	else:
		return map(chr,randomInts(start,end))  # randInts will generate random numbers in ASCII range and map will apply chr function to convert them to characters,remove this comment after reading



def randomInts(start = 0, end = 100,count = 100, unique = True):
	'''
	returns list of integers and uniqueness as parameter to
	allow duplicate entries in the list or not.
	'''
	#if unique numbers are required
	if unique:
		try:
		   return random.sample(range(start,end),count)
		except ValueError:
		   print('Sample size exceeded population size.')
	else:
		ans = []
		for i in xrange(count):
			ans.append(randomInt(start,end))
		return ans
