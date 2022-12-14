# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
# Решение оформлять в виде функций
# По возможности добавляйте docstring

# Функция для получения числа фибоначчи по его индексу
def fibo(n):
    if n in [1, 2]:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

# Получаем обыкновенный список чисел фибоначчи в зависиммости от введенного количества
def get_fibos_list(range_num):
    result_list = []
    for i in range(1, range_num + 1):
        result_list.append(fibo(i))
    return result_list

# Получаем список чисел фибоначчи для отрицательных и положительных чисел
def get_negafibo(list):
    result = []
    for item in range(len(list)):
        if ((len(list) - item) % 2 == 0):
            result.append(list[len(list) - item - 1] * -1)
        else:
            result.append(list[len(list) - item - 1])
    result.append(0)
    for item in range(len(list)):
        result.append(list[item])
    return result


print(f'Для k = 8 список Негафибоначчи =>  {get_negafibo(get_fibos_list(8))}')