# 3 - Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.



print("Программа, которая найдет палиндром введенного пользователем числа.")

input_string = input("Введите число для поиска палиндрома: ")

reverse_string = ""

while(True):
    for i in range(len(input_string)):
        reverse_string += input_string[len(input_string) - i - 1]

    print(f'{reverse_string}   \n')

    if(input_string != reverse_string):
        number = int(input_string) + int(reverse_string)
        input_string = str(number)
        reverse_string = ""
    else: break

print(f'Палиндромом введенного числа является - {reverse_string}')
