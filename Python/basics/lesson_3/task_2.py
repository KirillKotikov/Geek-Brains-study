# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
#  второй и предпоследний и т.д.

# Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

print("Программа, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.")

def sum_of_pairs(array):
    result = []
    for i in range(len(array)):
        if(i > len(array) - i - 1):
            break
        result.append(array[i] * array[len(array) - i - 1])
    return result

first_array = [2, 3, 4, 5, 6]
second_array = [2, 3, 5, 6]

print(f'Произведение пар чисел списка - {first_array} = {sum_of_pairs(first_array)}')
print(f'Произведение пар чисел списка - {second_array} = {sum_of_pairs(second_array)}')

