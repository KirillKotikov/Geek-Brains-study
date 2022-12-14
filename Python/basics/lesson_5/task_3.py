''' 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
    ['python', 'c#']
    [1,2]
    Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, 
    написанного большими буквами.
    [(1,'PYTHON'), (2,'C#')]
    Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, 
    с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
    [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
    [(1,'PYTHON'), (102,'C#')]
    Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. 
    Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
    Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
    Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком '''


languages = ['c#', 'python', 'java', 'go', 'scala', 'javascript']
numbers = [1, 2, 3, 4, 5, 6]

# создание кортежей через ZIP - получается как в описании задачи
cortege_list = list(zip(numbers, languages))

# Получает сумму очков слова
def get_sum_of_ord(word):
    result = 0
    for i in range(len(word)):
        result += ord(word[i])
    return result

# У меня не выходит сумма у 'c#' = 102. У меня выходит 134, в таблице вручную тоже проверял. Надеюсь это ошибка в задании.
# print(get_sum_of_ord("c#"))

# Узнает, есть ли порядковый номер в сумме очков
def ord_sum_contain_number(ord_sum, number):
    numbers_str = str(ord_sum)
    for i in range(len(numbers_str)):
        if str(number) == numbers_str[i]:
            return True
    return False

# Финальная функция :)
def filter_tuples_by_ord_sum(tuples):
    words_list = []
    numbers_list = []
    for i in range(len(tuples)):
        sum_of_ord = get_sum_of_ord(tuples[i].__getitem__(1))

        # Так можно проверить вручную правильность функции :)
        # print(tuples[i].__getitem__(0))
        # print(sum_of_ord, end='\n\n')

        if (ord_sum_contain_number(sum_of_ord, tuples[i].__getitem__(0))):
            numbers_list.append(sum_of_ord)
            words_list.append(tuples[i].__getitem__(1))
    return list(zip(numbers_list, words_list))

print(cortege_list)

print(filter_tuples_by_ord_sum(cortege_list))