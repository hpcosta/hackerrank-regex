'''
Created on 12 Dec 2016

@author: hpcosta
'''

# https://www.hackerrank.com/challenges/negative-lookbehind

Regex_Pattern = r"(?<![aeiouAEIOU])."   # Do not delete 'r'.


import re

Test_String = raw_input()

match = re.findall(Regex_Pattern, Test_String)

print "Number of matches :", len(match)