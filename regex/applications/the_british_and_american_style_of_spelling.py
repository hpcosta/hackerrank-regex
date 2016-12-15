'''
Created on 13 Dec 2016

@author: hpcosta
'''

# https://www.hackerrank.com/challenges/uk-and-us



n_lines = int(raw_input())

matches = 0
sentences = []
for i in range(0, n_lines):
   sentences.append(raw_input().strip())

sentence = ' '.join(sentences)  

testcases = int(raw_input())

for i in range(0, testcases):
   matches = 0
   word_1 = raw_input()
   word_2 = word_1[:-2] + 'se' 

   for word in sentence.split():
      #print('word: '+word)
      if word_1 == word or word_2 == word:
         matches+=1
   print(matches)

