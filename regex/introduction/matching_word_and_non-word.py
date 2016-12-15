'''
Created on 12 Dec 2016

@author: hpcosta
'''
# https://www.hackerrank.com/challenges/matching-word-non-word



Regex_Pattern = r"(\w){3}\W(\w){10}\W(\w){3}"   # Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())