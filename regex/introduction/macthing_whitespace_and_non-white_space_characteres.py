'''
Created on 12 Dec 2016

@author: hpcosta
'''
#https://www.hackerrank.com/challenges/matching-whitespace-non-whitespace-character


Regex_Pattern = r"(\S{2}\s){2}\S{2}"   # Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())