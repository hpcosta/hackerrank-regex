'''
Created on 12 Dec 2016

@author: hpcosta
'''

# https://www.hackerrank.com/challenges/matching-digits-non-digit-character

#10a10.2015452254 = true

import re
Regex_Pattern = r"^(\d{2}\D){2}\d{4}"   # Do not delete 'r'.
print(str(bool(re.search(Regex_Pattern, raw_input()))).lower())