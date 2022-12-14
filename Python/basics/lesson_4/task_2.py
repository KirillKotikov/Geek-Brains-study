''' 2 - Задайте последовательность чисел. Напишите программу, которая выведет список 
    неповторяющихся элементов исходной последовательности. Не использовать множества.
    [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]'''


testList = [1,1,1,1,2,2,2,3,3,3,4]

def getDistinctNumbers(list):
    result = []

    for i in list:
        if (not result.__contains__(i)):
            result.append(i)
    return result

print(getDistinctNumbers(testList))