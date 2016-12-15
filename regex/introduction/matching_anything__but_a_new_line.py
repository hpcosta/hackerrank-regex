'''
Created on 12 Dec 2016

@author: hpcosta
'''

# https://www.hackerrank.com/challenges/matching-anything-but-new-line


import re
import sys

test_string = raw_input()

regex_pattern = r"^(.{3}\.){3}.{3}$"   # Do not delete 'r'.

match = re.match(regex_pattern, test_string) is not None

print str(match).lower()

