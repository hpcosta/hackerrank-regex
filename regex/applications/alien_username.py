'''
Created on 15 Dec 2016

@author: hpcosta
'''

# https://www.hackerrank.com/challenges/alien-username




import re

# number of lines
n_lines = int(raw_input())


content = []
for i in range(0, n_lines):
   content.append(raw_input())
# content
str_content = ' '.join(content)


# number of test cases
n_test_cases = int(raw_input())
for j in range(0, n_test_cases):
   sub_word = raw_input().strip()
   print(len(re.findall(r'\b%s\b' % sub_word, str_content)))