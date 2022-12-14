# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. 
# Подумайте, как это можно решить с помощью рекурсии.

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10

print("Программа, которая будет преобразовывать десятичное число в двоичное.")

def dec_to_bin(number):
    result = ""
    temp = number % 2
    if (temp == 0):
        result = "0" + result
        number = number / 2
    elif (temp == 1):
        result = "1" + result
        number = (number - 1) / 2
    if(number != 1):
        return result + dec_to_bin(number)
    else: 
        result = "1" + result
        return result

print(f'Число 45 в двоичном виде = {dec_to_bin(45)}')
print(f'Число 3 в двоичном виде = {dec_to_bin(3)}')
print(f'Число 2 в двоичном виде = {dec_to_bin(2)}')
