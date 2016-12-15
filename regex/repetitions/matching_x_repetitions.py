'''
Created on 12 Dec 2016

@author: hpcosta
'''

# https://www.hackerrank.com/challenges/matching-x-repetitions


Regex_Pattern = r'^[02468\w]{40}[13579\s]{5}$'   # Do not delete 'r'.


import re

print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())