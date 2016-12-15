'''
Created on 13 Dec 2016

@author: hpcosta
'''

# https://www.hackerrank.com/challenges/detect-the-email-addresses

regex = r"[\w\.-]+@[\w\.-]+\b"   # Do not delete 'r'.

import re

n_lines = int(raw_input())


content = []
for i in range(0, n_lines):
   content.append(raw_input())

str_content = ' '.join(content)

emails =  re.findall(regex, str_content)

l = []
for email in emails:
   if email not in l:
      l.append(email)

l = sorted(l)
print(';'.join(l))