'''
Created on 19 Dec 2016

@author: hpcosta
'''

# https://www.hackerrank.com/challenges/hackerrank-language


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

dummy_list = 'C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC'.split(':')

n_tests = int(raw_input())
for i in range(0, n_tests):
   input = raw_input()
   #print(input[1])
   flag = False
   for lang in dummy_list:
      if bool(re.match(r'^(\d{5}\s)' + lang.lower() + '$', input.strip().lower())):
         flag = True
         break
   
   if flag:
      print('VALID')
   else:
      print('INVALID')