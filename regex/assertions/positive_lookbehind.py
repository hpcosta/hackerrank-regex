'''
Created on 13 Dec 2016

@author: hpcosta
'''

# https://www.hackerrank.com/challenges/positive-lookbehind

# Task
# 
# You have a test String S. 
# Write a regex which can match all the occurences of digit which are immediately preceded by odd digit.


Regex_Pattern = r"(?<=[13579])\d"   # Do not delete 'r'.

import re

Test_String = raw_input()

match = re.findall(Regex_Pattern, Test_String)

print "Number of matches :", len(match)



# Input (stdin)
# 123Go!
# Your Output (stdout)
# Number of matches : 1