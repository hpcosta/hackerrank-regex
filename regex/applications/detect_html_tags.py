'''
Created on 16 Dec 2016

@author: hpcosta
'''

# https://www.hackerrank.com/challenges/detect-html-tags/

import re

# number of lines
n_lines = int(raw_input())

content = []
for i in range(0, n_lines):
   content.append(raw_input())
str_content = ' '.join(content)

print(";".join(sorted(list(set(re.findall(r'<(\w+)>?', str_content))))))
