'''
Created on 13 Dec 2016

@author: hpcosta
'''
# https://www.hackerrank.com/challenges/alternative-matching

# Task
# 
# Given a test string, S , write a RegEx that matches S under the following conditions:
# 
# S must start with Mr., Mrs., Ms., Dr. or Er.
# The rest of the string must contain one or more English alphabetic letters (upper and lowercase).

Regex_Pattern = r'^(Mr|Mrs|Ms|Dr|Er)\.[a-zA-Z]+$'   # Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())




# Input (stdin)
# Mr.DOSHI
# Your Output (stdout)
# true