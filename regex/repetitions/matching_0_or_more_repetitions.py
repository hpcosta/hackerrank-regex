'''
Created on 12 Dec 2016

@author: hpcosta
'''
# https://www.hackerrank.com/challenges/matching-zero-or-more-repetitions



regex = r'^(\d){2,}[a-z]*[A-Z]*$'   # Do not delete 'r'.

import re

print(str(bool(re.search(regex, raw_input()))).lower())