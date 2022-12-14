from datetime import datetime

def read_logs():
    """ 
    Читает логи из файла-журнала и возвращает в виде текста
    """
    logs = ''
    with open('GB_python_lessons\lesson_7\logs.txt', 'r') as file:
        for line in file.readlines(): 
            logs += line
        file.close()
    return logs

def write_log(log):
    '''
    Записывает информацию из аргумента в журнал логов
    '''
    with open('GB_python_lessons\lesson_7\logs.txt', 'a') as file:
        file.write(f'{datetime.now()}:  {log}\n')
        file.close()