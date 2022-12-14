# 2- Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). 
# Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import random


print("\n")
print("Добро пожаловать в игру с конфетами :)", end="\n\n")

max_get_candies = 0
while (True):
    max_get_candies = input("Введите максимальное количество конфет, которое можно забрать за один ход -   ")
    if (max_get_candies.isdigit() and int(max_get_candies) > 1):
        break
    else: print("Вы ввели не число или число меньше 2!")
max_get_candies = int(max_get_candies)
print("\n")

number_of_candies = 0
while(True):
    number_of_candies = input(f'Введите общее количество конфет, которое должно быть больше {max_get_candies} -   ')
    if (number_of_candies.isdigit() and int(number_of_candies) > 1 and int(number_of_candies) > max_get_candies):
        break
    else: print(f'Вы ввели не число или число меньше {max_get_candies}!')
number_of_candies = int(number_of_candies)
print("\n")

ai = False
while(True):
    mode = input("Противником будет человек или компьютер? Ответы: ч - человек, к - компьютер. Введите ч или к -   ")
    if (mode.lower() == "к"):
        ai = True
        break
    elif (mode.lower() == "ч"):
        break
    else: print("Вы ввели некорректный ответ")

print("\n")
game_mode = "Вы выбрали игру с компьютером!" if ai else "Вы выбрали игру с человеком!"
first_turn = True if random.randint(1, 2) == 1 else False
enemy = "компьютер" if ai else "ВТОРОЙ игрок"
first_player = "Первым ходит ПЕРВЫЙ игрок!" if first_turn else f'Первым ходит {enemy}!'
print(f'Игра начинается! {game_mode} Общее количество конфет = {number_of_candies}, за один ход можно взять от 1 по {max_get_candies} конфет.')
print(f'Проигрывает тот, кто забирает последнюю конфету. Очередность хода определяется случайно. {first_player}')

if (ai == True):

    while(number_of_candies > 0):
        if (first_turn):
            while True:
                first_turn = True
                max_get_candies = max_get_candies if max_get_candies <= number_of_candies else number_of_candies
                move_one = input(f'Ваш ход! На столе {number_of_candies} конфет. Введите количество конфет от 1 по {max_get_candies} -   ')
                if (move_one.isdigit() and int(move_one) > 0 and int(move_one) <= max_get_candies):
                    number_of_candies -= int(move_one)
                    first_turn = False
                    break
                else: print(f'Вы ввели не число или число больше {max_get_candies}!')
            if(number_of_candies < 1): break

        if(not first_turn):
            max_get_candies = max_get_candies if max_get_candies <= number_of_candies else number_of_candies
            move_two = 1

            if (number_of_candies == max_get_candies and number_of_candies > 1):
                 move_two = max_get_candies -1
            elif (number_of_candies <= (max_get_candies * 2)):
                move_two = number_of_candies - max_get_candies - 1
            elif (number_of_candies > max_get_candies + 1):
                move_two = number_of_candies % (max_get_candies - 1)
                if (move_two == 0): move_two = max_get_candies - 1

            number_of_candies -= move_two
            print(f'Компьютер сделал свой ход! Он взял {move_two} конфет!')
            first_turn = True
    
    winner = "Поздравляю! Вы победили!" if first_turn else "Увы, Вы проиграли."
    print(winner)

else:
    while(number_of_candies > 0):  
        if(first_turn):
            while True:
                max_get_candies = max_get_candies if max_get_candies <= number_of_candies else number_of_candies
                move_one = input(f'Ходит первый игрок! На столе {number_of_candies} конфет. Введите количество конфет от 1 по {max_get_candies} -   ')
                if (move_one.isdigit() and int(move_one) > 0 and int(move_one) <= max_get_candies):
                    number_of_candies -= int(move_one)
                    first_turn = False
                    break
                else: print(f'Вы ввели не число или число больше {max_get_candies}!')

        else:
            while True:
                max_get_candies = max_get_candies if max_get_candies <= number_of_candies else number_of_candies
                move_two = input(f'Ходит второй игрок! На столе {number_of_candies} конфет. Введите количество конфет от 1 по {max_get_candies} -   ')
                if (move_two.isdigit() and int(move_two) > 0 and int(move_two) <= max_get_candies):
                    number_of_candies -= int(move_two)
                    first_turn = True
                    break
                else: print(f'Вы ввели не число или число больше {max_get_candies}!')
    
    winner = "Поздравляем ПЕРВОГО игрока! Он победил!" if first_turn else "Поздравляем ВТОРОГО игрока! Он победил!"
    print(winner)