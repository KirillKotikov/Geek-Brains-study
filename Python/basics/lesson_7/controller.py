import calc
import ui
import logger

def button_menu():
    '''
    В зависимости от входящей команды выполняет вычисления с числами
    ''' 
    while True:
        x = 0
        y = 0
        data = ''
        command = input("Введите номер команды (1 сложить, 2 вычесть, 3 умножить, 4 поделить, 5 посмотреть журнал вычислений, 6 выйти) - ")

        if command == "6":
            ui.view_result("До свидания!")
            exit()

        if command == "1": 
            x = ui.get_input_number("первое") 
            y = ui.get_input_number('второе')
            data = str(f'{x} + {y} = {calc.sum(x, y)}')
            ui.view_result(data) 
            logger.write_log(data)
        elif command == "2": 
            x = ui.get_input_number("первое") 
            y = ui.get_input_number('второе')
            data = str(f'{x} - {y} = {calc.sub(x, y)}')
            ui.view_result(data) 
            logger.write_log(data)
        elif command == "3": 
            x = ui.get_input_number("первое") 
            y = ui.get_input_number('второе')
            data = str(f'{x} * {y} = {calc.mult(x, y)}')
            ui.view_result(data) 
            logger.write_log(data)
        elif command == "4": 
            x = ui.get_input_number("первое") 
            y = ui.get_input_number('второе')
            data = str(f'{x} / {y} = {calc.div(x, y)}')
            ui.view_result(data) 
            logger.write_log(data)
        elif command == "5": 
            ui.view_result(logger.read_logs())
        else:
            ui.view_result('Вы ввели неверную команду!')

            
        