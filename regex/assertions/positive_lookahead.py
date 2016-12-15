'''
Created on 13 Dec 2016

@author: hpcosta
'''
# https://www.hackerrank.com/challenges/positive-lookahead


# Task
# 
# You have a test string S. 
# Write a regex that can match all occurrences of o followed immediately by oo in .

Regex_Pattern = r'o(?=oo)'   # Do not delete 'r'.

import re

Test_String = raw_input()

match = re.findall(Regex_Pattern, Test_String)

print "Number of matches :", len(match)



# Input (stdin)
# gooooo!
# Your Output (stdout)
# Number of matches : 3