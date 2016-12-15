'''
Created on 12 Dec 2016

@author: hpcosta
'''
# https://www.hackerrank.com/challenges/matching-start-end

Regex_Pattern = r"^(\d)(\w){4}\.$"   # Do not delete 'r'.


import re

print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())