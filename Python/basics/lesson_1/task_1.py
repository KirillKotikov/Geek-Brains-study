
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

print("Программа, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.")
day_number = int(input("Введите число дня недели от 1 до 7: "))
if (day_number == 6) or (day_number == 7):
    print(f'{day_number} -> Да')
else:
    print(f'{day_number} -> Нет')
