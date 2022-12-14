

def check_number(string):
    """ 
    Проверяет, является ли строка рациональным или комплексным числом. 
    При положительном результате возвращает кортеж (True, число).
    При отрицательном возвращает - False.    
    """
    try:
        float(string)
        return True, float(string)
    except ValueError:
        try:
            complex(string)
            return True, complex(string)
        except ValueError:
            print (f'Введенное значение -> {string} не является рациональным или комплексным числом!')
            return False
            