'''
Created on 12 Dec 2016

@author: hpcosta
'''

# https://www.hackerrank.com/challenges/matching-one-or-more-repititions

regex = r'^\d+[A-Z]+[a-z]+$'   # Do not delete 'r'.

import re

print(str(bool(re.search(regex, raw_input()))).lower())