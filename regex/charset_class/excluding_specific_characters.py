'''
Created on 12 Dec 2016

@author: hpcosta
'''
# https://www.hackerrank.com/challenges/excluding-specific-characters


regex = r'^[^\d][^a-z][^b,c,D,F][^\s][^A,E,I,O,U][^\.,]$'   # Do not delete 'r'.



import re

print(str(bool(re.search(regex, raw_input()))).lower())