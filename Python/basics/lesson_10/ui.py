PHONE_NUMBER_IS_INVALID = "Вы ввели некорректный номер телефона! Он должен быть в формате +79239232233 или -."
contact = []

def view(list):
    '''
    Функция принимает на вход лист c листами строк и возвращает строку с данными
    '''
    phone_book = ''
    for line in list:
        for string in line:
            phone_book += string
        phone_book += '\n'
    return phone_book