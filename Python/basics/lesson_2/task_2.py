# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial(n):
    result = 1
    for i in range(n):
        result *= i + 1
    return result

print("Программа, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.")

while True:
    n = input("Введите натуральное число N: ")
    if n.isdigit():
        print("[ ", end='')
        number_n = int(n)
        for i in range(number_n):
            if i == number_n - 1:
                print(f'{factorial(i+1)}', end='')
            else: 
                print(f'{factorial(i+1)}, ', end='')
        print(" ]")
        break
    print("Вы ввели неверные данные!") 