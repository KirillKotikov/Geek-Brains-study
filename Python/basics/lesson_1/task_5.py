# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print("Программа, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.")
x1 = int(input("Введите значение х1 = "))
y1 = int(input("Введите значение y1 = "))
x2 = int(input("Введите значение х2 = "))
y2 = int(input("Введите значение y2 = "))

distance = round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)

print(f'Расстояние между точками (x1 = {x1}, y1 = {y1} и x2 = {x2}, y2 = {y2}) = {distance}') 