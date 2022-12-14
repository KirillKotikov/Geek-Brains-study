'''3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)'''

crd_one = '1 6 -3'
crd_two = '-5 -1 5'

first = list(map(lambda x: int(x), crd_one.split(' ')))
second = list(map(lambda x: int(x), crd_two.split(' ')))

print((sum(list(map(lambda x: x*x, list(map(lambda x, y: y - x, first, second)))))) ** 0.5)
