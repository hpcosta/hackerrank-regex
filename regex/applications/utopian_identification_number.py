'''
Created on 2 Jan 2017

@author: hpcosta
'''

# https://www.hackerrank.com/challenges/utopian-identification-number

regex = r"^[a-z]{0,3}\d{2,8}[A-Z]{3,}"   # Do not delete 'r'.

import re

n_lines = int(raw_input())

for i in range(0, n_lines):
   content = raw_input()
   if bool(re.match(regex, content)):
      print('VALID')
   else:
      print('INVALID')
