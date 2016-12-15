'''
Created on 15 Dec 2016

@author: hpcosta
'''
# https://www.hackerrank.com/challenges/detecting-valid-latitude-and-longitude

import re
regex = r'^\([+-]?(([1-8]?[0-9]|0)(\.\d+)?|90(\.0+)?),[ ]?[+-]?(([1]?[1-7]?[0-9]|0|[1-9][0-9]|10[0-9])(\.\d+)?|180(\.0+)?)\)$'

n_tests = int(raw_input())
for i in range(0, n_tests):
   if bool(re.match(regex, raw_input())):
      print("Valid")
   else:
      print("Invalid")