import check

def get_input_number(serial_number = ''):
    """ 
    Функция получения строки (числа) от пользователя и преобразования его в число. 
    Возвращает преобразованное число.
    """
    number = input(f'Введите {serial_number} число - ')
    while not check.check_number(number):
        number = input(f'Введите {serial_number} число - ')
    return check.check_number(number)[1]

def view_result(result):
    '''
    Выводит на экран строку из аргумента
    '''
    print(result)


