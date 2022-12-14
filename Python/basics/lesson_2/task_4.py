# 4 - Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)


from datetime import datetime

def random(min, max):
    result = datetime.now().microsecond
    while(result < min or result > max):
        result = result >> 1
        print(result)
    return result

print("Программа для выдачи случайного числа")
while(True):
    min_num = int(input("Введите минимальное натуральное число: "))
    max_num = int(input("Введите максимальное натуральное число: "))
    print(random(min_num, max_num))

