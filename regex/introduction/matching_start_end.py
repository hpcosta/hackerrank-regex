'''
Created on 12 Dec 2016

@author: hpcosta
'''
# https://www.hackerrank.com/challenges/matching-start-end

regex = r"^(\d)(\w){4}\.$"   # Do not delete 'r'.


import re

print(str(bool(re.search(regex, raw_input()))).lower())