'''
Created on 2 Jan 2017

@author: hpcosta
'''

# https://www.hackerrank.com/challenges/find-hackerrank



import re

# number of lines
n_lines = int(raw_input())

for i in range(0, n_lines):
   content = raw_input().strip()
   match1 = re.match('^(hackerrank).*', content)
   match2 = re.match('.*(hackerrank)$', content)
   match3 = re.match('^(hackerrank)$', content)
   
   if match3:
      print(0)
   elif match1:
      print(1)
   elif match2:
      print(2)
   else:
      print(-1)