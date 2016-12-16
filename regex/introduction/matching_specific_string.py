'''
Created on 12 Dec 2016

@author: hpcosta
'''


# https://www.hackerrank.com/challenges/matching-specific-string
import re

Test_String = raw_input()
regex = r'hackerrank'   # Do not delete 'r'.
match = re.findall(regex, Test_String)

print "Number of matches :", len(match)