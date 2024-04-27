import mmh3
import jhashcode
import re

def bloom_size(input):
    bloom_size = 4 * len(input)		# n/m = 4, thus n = 4 * m
    return bloom_size

def initialize_bloom (size):
    bloom_filter=[0]*size        # bit_array_size is 4 * size of Spam data
    return bloom_filter

def hash_fun_01(email,bloom_size):
    return (mmh3.hash(email) % bloom_size)
	
def hash_fun_02(email,bloom_size):
	return (jhashcode.hashcode(email) % bloom_size)

def hash_fun_03(email,bloom_size):
 	return ((sum(ord(char) for char in email))% bloom_size)

def format_input(input):
    #turn all letters into lowercase
    input= input.lower()

    # To remove extra spaces split the string into words then join them back with a single space.
    input = input.split()
    input= ' '.join(input)

    #remove_punctuation
    input= re.sub(r'[^\w\s]', '', input)
    
    return input 