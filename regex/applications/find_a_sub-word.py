'''
Created on 15 Dec 2016

@author: hpcosta
'''
# https://www.hackerrank.com/challenges/find-substring


# we will need a positive lookbehind and lookahead
positive_lookbehind = r"(?<=\w)"   
positive_lookahead = r"(?=\w)"

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
   print(len(re.findall(r'(?<=\w)%s(?=\w)' % sub_word, str_content)))
