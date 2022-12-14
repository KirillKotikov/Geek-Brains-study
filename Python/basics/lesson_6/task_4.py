'''4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
Примеры
список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
список: [], ищем: "123", ответ: -1'''

lst = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
srch_str = 'qwe'
search_indexes = list(filter(lambda x: lst[x] == srch_str, [y for y in (range(0, len(lst)))]))
print(search_indexes[1] if len(search_indexes) > 1 else -1)


lst = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
srch_str = 'йцу'
search_indexes = list(filter(lambda x: lst[x] == srch_str, [y for y in (range(0, len(lst)))]))
print(search_indexes[1] if len(search_indexes) > 1 else -1)


lst = ["йцу", "фыв", "ячс", "цук", "йцукен"]
srch_str = 'йцу'
search_indexes = list(filter(lambda x: lst[x] == srch_str, [y for y in (range(0, len(lst)))]))
print(search_indexes[1] if len(search_indexes) > 1 else -1)


lst = ["123", "234", 123, "567"]
srch_str = '123'
search_indexes = list(filter(lambda x: lst[x] == srch_str, [y for y in (range(0, len(lst)))]))
print(search_indexes[1] if len(search_indexes) > 1 else -1)

lst = []
srch_str = '123'
search_indexes = list(filter(lambda x: lst[x] == srch_str, [y for y in (range(0, len(lst)))]))
print(search_indexes[1] if len(search_indexes) > 1 else -1)



