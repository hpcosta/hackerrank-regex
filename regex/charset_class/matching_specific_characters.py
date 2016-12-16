'''
Created on 12 Dec 2016

@author: hpcosta
'''

# https://www.hackerrank.com/challenges/matching-specific-characters


regex = r'^[123][120][xs0][30Aa][xsu][\.,]$'   # Do not delete 'r'.


import re

print(str(bool(re.search(regex, raw_input()))).lower())