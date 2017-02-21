'''
This file contains the functions that generate
data, in different formats and provide that as stdin to files

'''

import os
import random

MIN_INT = -100000000000000000000
MAX_INT = 100000000000000000000

def randomInt(start = 0 ,end = 100):
	'''
	returns any random number between start-end (inclusive)
	'''
	try:
		if start <= end and (start >= MIN_INT and end <= MAX_INT) and (end >= MIN_INT and end <= MAX_INT):
	        output = random.randint(start,end)
	        if output >= MIN_INT and output <= MAX_INT:
	            return output
	        else:
	            raise ValueError("Output is out of bound !")
	    else:
	        raise ValueError("Input arguments !" )
	except ValueError as e:
		print (e)


def randomAlpha(start = 97, end = 122):
	'''
	returns any random Alphabet between A-Z or a-z (inclusive)
	if case not specified give lowercase letter
	'''
	try:
		if start < end:
			if (start >= 97 and start <= 122) and (end >= 97 and end <= 122):
				output = chr(randomInt(start, end))
				if output >= 'a' and output <= 'z':
					return output
				else:
					print "Invalid Output !"
			elif start >= 65 and start <= 90 and end >= 65 and end <= 90:
				 output = chr(randomInt(start, end))
				 if output >= 'A' and output <= 'z':
					 return output
				 else:
					 raise ValueError("Invalid Output!")
			else:
				raise ValueError("Invalie arguments")
		else:
			raise ValueError("Invalid arguments !")
	except ValueError as e:
		print(e)


def randomAscii(start = 0,end = 255,range = True):
	'''
	returns any random ASCII character (0-255) (inclusive)
	'''
	try:
		if (start >= 0 and start <= 255) and (end >= 0 and end <= 255) and (end >= start): #constraints check
	        if range == True or range == False:
				if not range:
					output = chr(randomInt(start,end))
				else:
					output = map(chr,randomInts(start,end))
	            if range == True:
	                if min(output) >= 0 and max(output) <=255:
	                    return output
	                else:
	                    raise ValueError("Invalie Output !")
	            else:
	                if output >=0 and output <=255:
	                    return output
	                else:
	                    raise ValueError("Invalid Output")

	        else:
	            raise ValueError("Invalid arguments !")
	except ValueError as e:
		print (e)




def randomInts(start = 0, end = 100,count = 100, unique = True):
	'''
	returns list of integers and uniqueness as parameter to
	allow duplicate entries in the list or not.
	'''
	try:
		if end >= start and (start >=MIN_INT and start<= MAX_INT) and (start >=MIN_INT and start<= MAX_INT):
			if unique == True or unique == False:
				#if unique numbers are required
				if unique:
					try:
					   output = random.sample(range(start,end),count)
					except ValueError:
					   print('Sample size exceeded population size.')
				else:
					output = []
					for i in xrange(count):
						output.append(randomInt(start,end))
					return output
				if min(output) >= MIN_INT and max(utput) <= MAX_INT:
		            return output
		        else:
		            raise ValueError("Invalid Output")
	        else:
	            raise ValueError("Invalid arguments !")
	    else:
	        raise ValueError("Invalid arguments !")
	except ValueError as e:
		print (e)
