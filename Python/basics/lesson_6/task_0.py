'''Задание с семинара
Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,. приоритет операций стандартный.
Дополнительное задание: Добавьте возможность использования скобок, меняющих приоритет операций
*Пример:
2+2 => 4;
1+2*3 => 7;

10/2*5 => 25;
10 * 5 * => недостаточно числовых данных
-5 + 5 => 0
два + три => неправильный ввод: нужны числа
(2+((5-3)*(16-14)))/3 => 2
(256 - 194 => некорректная запись скобок'''

# METHODS:
def brackets_checking(input_text):
    result_list = []
    count1 = 0
    count2 = 0 
    for ch in input_text:
        if ch == '(':
            count1 += 1
        elif ch == ')':
            count2 += 1     
    if count2 != count1:
        print(f'Некорректная запись скобок в выражении -> {input_text}')
        result_list.append(False)
    else: 
        result_list.append(True)
        result_list.append(count1)
    return result_list

def get_numbers(expression):
    numbers = []
    temp = ''
    expression += '='
    for char in expression:
        if char.isdigit():
            temp += char 
        else:
            numbers.append(temp)
            temp = ''
    return list(map(lambda x: int(x), list(filter(lambda x: x.isdigit(), numbers))))

def get_operators(expression):
    return list(filter(lambda x: x in '-+*/', expression))

def check_alpha(expression):
    return not any(filter(lambda x: x.isalpha(), expression))

def check_expressions(numbers: list, operators: list):
    return True if len(numbers) > len(operators) else False 

def main_function(numbers: list, operators: list):
    while (operators.__contains__('*') or operators.__contains__('/')):
        for i in range(len(operators)):
            if (operators[i] == '*' or operators[i] == '/'):    
                firs_number = numbers.pop(i)
                second_number = numbers.pop(i)
                operator = operators.pop(i)
                if(operator == '*'):
                    numbers.insert(i, firs_number * second_number)
                elif(operator == '/'):
                    numbers.insert(i, firs_number / second_number)

    while(len(numbers) > 1):
        count = 0
        firs_number = numbers.pop(count)
        second_number = numbers.pop(count)
        operator = operators.pop(count)
        if(operator == '+'):
            numbers.insert(count, firs_number + second_number)
        elif(operator == '-'):
            numbers.insert(count, firs_number - second_number)
        count += 1


#     ACTION :)
numbers = []
operators = []
expression = '25+4*3-22*8'
print(eval(expression))
print()


if check_alpha(expression):
    numbers = get_numbers(expression)
    operators = get_operators(expression)
    if check_expressions(numbers, operators) == False:
        print("Выражение неполное!")
    else: 
        check_brackets = brackets_checking(expression)
        if (check_brackets[0] and check_brackets[1] > 0):
            input_brackets_count = check_brackets[1]
            split_string = expression.split('(')[input_brackets_count - 1].split(')')[0]
        elif (check_brackets[0]):
            main_function(numbers, operators)
            print(numbers[0])
else: print("вы ввели буквы!")


