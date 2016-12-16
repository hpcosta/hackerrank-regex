'''
Created on 13 Dec 2016

@author: hpcosta
'''

# https://www.hackerrank.com/challenges/split-number



regex = r"(\d{1,3})[\s-](\d{1,3})[\s-](\d{4,10})"   # Do not delete 'r'.

import re

n_lines = int(raw_input())

number = ''
local_area_code = ''
contry_code = ''

for i in range(0, n_lines):
   match = re.search(regex, raw_input())
   print "CountryCode=" + match.group(1) + ",LocalAreaCode=" + match.group(2) + ",Number=" + match.group(3)
   
