'''
Created on 12 Dec 2016

@author: hpcosta
'''
# https://www.hackerrank.com/challenges/matching-zero-or-more-repetitions



Regex_Pattern = r'^(\d){2,}[a-z]*[A-Z]*$'   # Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())