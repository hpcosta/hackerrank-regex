'''
Created on 2 Jan 2017

@author: hpcosta
'''

# https://www.hackerrank.com/challenges/valid-pan-format

regex = r"^[A-Z]{5}\d{4}[A-Z]$"   

import re

n_lines = int(raw_input())

for i in range(0, n_lines):
   content = raw_input()
   if bool(re.match(regex, content)):
      print('YES')
   else:
      print('NO')
