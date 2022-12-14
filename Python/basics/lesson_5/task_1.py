''' 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
'абвгдейка - это передача' = >" - это передача" '''

import re

text = 'абвгдейка - это передача'
words = text.split(' ')
fragment = 'абв'
new_words = []

for word in words:
     if fragment not in word:
         new_words.append(word)
         
result = ' '.join(new_words)

print(text)
print(result)
