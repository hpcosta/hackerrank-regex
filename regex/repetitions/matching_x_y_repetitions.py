'''
Created on 12 Dec 2016

@author: hpcosta
'''

# https://www.hackerrank.com/challenges/matching-x-y-repetitions


regex = r'^(\d){1,2}[a-zA-Z]{3,}(\D){0,3}$'   # Do not delete 'r'.

import re

print(str(bool(re.search(regex, raw_input()))).lower())