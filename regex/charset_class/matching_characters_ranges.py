'''
Created on 12 Dec 2016

@author: hpcosta
'''

# https://www.hackerrank.com/challenges/matching-range-of-characters
regex = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'   # Do not delete 'r'.
import re

print(str(bool(re.search(regex, raw_input()))).lower())