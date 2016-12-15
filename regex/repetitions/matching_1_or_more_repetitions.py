'''
Created on 12 Dec 2016

@author: hpcosta
'''

# https://www.hackerrank.com/challenges/matching-one-or-more-repititions

Regex_Pattern = r'^\d+[A-Z]+[a-z]+$'   # Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())