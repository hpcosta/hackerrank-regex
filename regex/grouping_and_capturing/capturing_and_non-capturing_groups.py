'''
Created on 13 Dec 2016

@author: hpcosta
'''
# https://www.hackerrank.com/challenges/capturing-non-capturing-groups

# Task
# 
# You have a test String S. 
# Your task is to write a regex which will match S with the following condition:
# 
# S should have 3 or more consecutive repetitions of ok.

Regex_Pattern = r'(?:ok){3,}'   # Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())


# Input (stdin)
# okokok! cya
# Your Output (stdout)
# true