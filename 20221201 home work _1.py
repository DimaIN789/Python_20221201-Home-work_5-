# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


print()
with open('5.txt', 'r', encoding = 'utf_8') as data:
    stroka = data.read().split()
print(f'В файле записано: {stroka}')
print('Удалили все слова с абв и получили: ')
print(' '.join([word for word in stroka if 'абв' not in word]))
print()








