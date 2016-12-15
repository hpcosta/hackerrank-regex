'''
Created on 13 Dec 2016

@author: hpcosta
'''
# https://www.hackerrank.com/challenges/backreferences-to-failed-groups

Regex_Pattern = r"^\d{2}(-?)\d{2}\1\d{2}\1\d{2}$"   # Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())



# Task
# 
# You have a test string S. 
# Your task is to write a regex which will match S, with following condition(s):
# 
# S consists of 8 digits.
# S may have "-" separator such that string S gets divided in 4 parts, with each part having exactly two digits. (Eg. 12-34-56-78)
# Valid 
# 
# 12345678
# 12-34-56-87
# Invalid 
# 
# 1-234-56-78
# 12-45-7810