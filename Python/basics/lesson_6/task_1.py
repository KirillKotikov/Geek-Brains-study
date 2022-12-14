'''1- Определить, присутствует ли в заданном списке строк, некоторое число'''

strings = ['123', 'cake', 'joo', '34', 'foo', 'Main', '89']
search_str = '34'

if len(list(filter(lambda x: x == search_str, strings))) > 0:
    print(True)
else: print(False)