'''
Created on 13 Dec 2016

@author: hpcosta
'''
# https://www.hackerrank.com/challenges/matching-word-boundaries


# Task
# 
# You have a test String S. 
# Your task is to write a regex which will match word starting with vowel (a,e,i,o, u, A, E, I , O or U). 
# The matched word can be of any length. The matched word should consist of letters (lowercase and uppercase both) only. 
# The matched word must start and end with a word boundary.

# input: Found any match?
# output: true

regex = r'\b[aeiouAEIOU][a-zA-Z]*\b'   # Do not delete 'r'.


import re

print(str(bool(re.search(regex, raw_input()))).lower())