'''5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.'''

from tkinter import N


digits = [123, 12, 65, 84, 25, 43, 86, 35, 90]

first_part = digits[:int(len(digits)/2):]
second_part = list(reversed(digits[int(len(digits)/2)::]))

result = list(map(lambda x, y: x + y, first_part, second_part))
if (len(digits) % 2 != 0): 
    result.append(second_part[-1])

print(result)