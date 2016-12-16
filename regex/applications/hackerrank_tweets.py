'''
Created on 16 Dec 2016

@author: hpcosta
'''

# https://www.hackerrank.com/challenges/hackerrank-tweets


import re

# number of lines
n_lines = int(raw_input())

content = []
for i in range(0, n_lines):
   content.append(raw_input().lower())
str_content = ' '.join(content)

print(len(re.findall(r'hackerrank', str_content)))
