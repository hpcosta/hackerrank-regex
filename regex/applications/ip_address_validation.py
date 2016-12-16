'''
Created on 16 Dec 2016

@author: hpcosta
'''

# https://www.hackerrank.com/challenges/ip-address-validation


import re
regex_ipv4 = r'^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$'
regex_ipv6 = r'^((([0-9]|[a-f])?){3}([0-9]|[a-f]):){7}(([0-9]|[a-f])?){3}([0-9]|[a-f])$'

#print(bool(re.match(regex_ipv4, "253.231.111.64")))
#print(bool(re.match(regex_ipv6, "1050:0:0:0:5:600:300c:326b")))
n_tests = int(raw_input())
for i in range(0, n_tests):
   ip = raw_input()
   if bool(re.match(regex_ipv4, ip)):
      print("IPv4")
   elif bool(re.match(regex_ipv6, ip)):
      print("IPv6")
   else:
      print("Neither")