'''
Created on 12 Dec 2016

@author: hpcosta
'''


# https://www.hackerrank.com/challenges/matching-specific-string
import re

Test_String = raw_input()
Regex_Pattern = r'hackerrank'   # Do not delete 'r'.
match = re.findall(Regex_Pattern, Test_String)

print "Number of matches :", len(match)