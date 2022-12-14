''' 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, 
которые имеют средний балл более «4».
Нужно перезаписать файл.
Пример:
Ангела Меркель 5
Андрей Валетов 5
Фредди Меркури 3
Анастасия Пономарева 4

Программа выдаст:
АНГЕЛА МЕРКЕЛЬ 5
АНДРЕЙ ВАЛЕТОВ 5
Фредди Меркури 3
Анастасия Пономарева 4 '''


inputLines = []
with open('lesson_4/task_3_input_file.txt', 'r') as file:
    inputLines = file.readlines()

outputLines = []
for line in inputLines:
    if (line.__contains__("5")):
        outputLines.append(line.upper())
    else:
        outputLines.append(line)

with open('lesson_4/task_3_input_file.txt', 'w') as file:
    for line in outputLines:
        file.write(line)