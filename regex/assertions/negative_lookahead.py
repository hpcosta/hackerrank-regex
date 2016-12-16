'''
Created on 13 Dec 2016

@author: hpcosta
'''

# https://www.hackerrank.com/challenges/negative-lookahead


# Task
# 
# You have a test String S. 
# Write a regex which can match all characters which are not immediately followed by that same character.
# 
# Example
# 
# If S  = goooo, then regex should match g ooo o. Because the first g is not follwed by g and the last o is not followed by o.


regex = r"(.)(?!\1)"   # Do not delete 'r'.

import re

Test_String = raw_input()

match = re.findall(regex, Test_String)

print "Number of matches :", len(match)



# Input (stdin)
# gooooo
# Your Output (stdout)
# Number of matches : 2