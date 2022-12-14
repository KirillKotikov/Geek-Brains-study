'''6-Сформировать список из N членов последовательности.
Для N = 5: 1, -3, 9, -27, 81 и т.д'''

n = 5
lst = []

list(map(lambda x: lst.append(1 if x == 0 else lst[-1] * -3), [y for y in range(n)]))

print(lst)