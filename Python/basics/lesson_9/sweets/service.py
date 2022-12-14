import random
import logging

# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

max_get_candies = 0
number_of_candies = 0
ai = False
first_turn = True if random.randint(1, 2) == 1 else False

def game_mode(): return "Компьютером" if ai else "Человеком"
def start_game(): return f'Игра начинается! Вы выбрали игру с {game_mode()}! Общее количество конфет = {number_of_candies}, за один ход можно взять от 1 по {max_get_candies} конфет.\n Проигрывает тот, кто забирает последнюю конфету. Очередность хода определяется случайно. {first_player()}\n'
def next_move(): return f'{move_player()} На столе {number_of_candies} конфет. Введите количество конфет от 1 по {max_get_candies}:'

def first_player():
    '''Выводит нужную запись в случае первого хода компьютера'''
    if ai:
        if not first_turn:
            return "Первым ходит компьютер!\n"
        else: return ''
    else:
        return ''

def move_player(): 
    '''Возвращает информацию об очередности хода'''
    if ai:
        if first_turn:
            return "Сейчас ВАШ ход!"
    else:
        if first_turn:
            return "Сейчас ходит ПЕРВЫЙ игрок!"  
        else: return "Сейчас ходит ВТОРОЙ игрок!"  

def winner(): 
    '''Возвращает информацию о победителе'''
    if ai:
        if first_turn:
            return 'Поздравляем! Вы победили!'
        else:
            return 'Победил компьютер! Вы проиграли :('
    else:
        if first_turn:
            return 'Поздравляем ПЕРВОГО игрока! Он победил!'
        else: return 'Поздравляем ВТОРОГО игрока! Он победил!'

def validate_max_get_candies(max_get_candies):
    '''Проверяет валидность введенного количества конфет'''
    if (max_get_candies.isdigit() and int(max_get_candies) > 1):
        return True
    else: return False

def validate_number_of_candies(number_of_candies):
    '''Проверяет валидность введенного количества всех конфет'''
    global max_get_candies
    if (number_of_candies.isdigit() and int(number_of_candies) > 1 and int(number_of_candies) > max_get_candies):
        return True
    else: return False

def computer_move():
    '''Логика хода компьютера'''
    global max_get_candies
    global number_of_candies
    max_get_candies = max_get_candies if max_get_candies <= number_of_candies else number_of_candies
    move_two = 1
    if (number_of_candies > 1):
        if (number_of_candies == max_get_candies):
                move_two = max_get_candies -1
        elif (number_of_candies == max_get_candies + 1):
            move_two = max_get_candies
        elif (number_of_candies <= (max_get_candies * 2)):
            move_two = number_of_candies - max_get_candies - 2
        elif (number_of_candies > max_get_candies + 1):
            move_two = number_of_candies % (max_get_candies - 1)
            if (move_two == 0): 
                move_two = max_get_candies - 1
    global first_turn
    first_turn = True
    logger.info("Компьютер взял %s конфет.", move_two)
    number_of_candies -= move_two
    if number_of_candies < max_get_candies: max_get_candies = number_of_candies
    return f'Компьютер сделал свой ход! Он взял {move_two} конфет!'

def validation_move(mess):
    '''Проверка хода игрока'''
    global max_get_candies
    global number_of_candies
    max_get_candies = max_get_candies if max_get_candies <= number_of_candies else number_of_candies
    if (mess.isdigit() and int(mess) > 0 and int(mess) <= max_get_candies):
        return True
    else:
        return False 

def human_move(mess):
    '''локига вычислений хода игрока'''
    global number_of_candies
    global max_get_candies
    global first_turn
    number_of_candies -= int(mess) 
    first_turn = not first_turn
    if number_of_candies < max_get_candies: max_get_candies = number_of_candies

def restart():
    '''Обнуление всех параметров'''
    global max_get_candies
    global number_of_candies
    global ai
    global first_turn
    max_get_candies = 0
    number_of_candies = 0
    ai = False
    first_turn = True if random.randint(1, 2) == 1 else False