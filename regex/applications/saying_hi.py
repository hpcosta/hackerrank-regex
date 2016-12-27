'''
Created on 27 Dec 2016

@author: hpcosta
'''

# https://www.hackerrank.com/challenges/saying-hi


import re
regex = r"^[Hh][Ii]\s[^Dd].*"   

# number of lines
n_test_cases = int(raw_input())
for j in range(0, n_test_cases):
   sentence = raw_input().strip()
   if(bool(re.match(regex, sentence))):
      print(sentence)