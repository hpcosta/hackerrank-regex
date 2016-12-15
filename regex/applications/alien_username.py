'''
Created on 15 Dec 2016

@author: hpcosta
'''

# https://www.hackerrank.com/challenges/alien-username


import re
regex = r'^[\_\.](?=[0-9]+)\d*[a-zA-Z]*_?$'

n_tests = int(raw_input())
for i in range(0, n_tests):
   if bool(re.match(regex, raw_input())):
      print("Valid".upper())
   else:
      print("Invalid".upper())