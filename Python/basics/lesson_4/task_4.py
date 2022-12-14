''' 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. 
    При расшифровке происходит обратная операция. К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. 
    "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
    Сдвиг часто называют ключом шифрования.
    Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, 
    считывает текст и дешифровывает его.'''

    # Functions:

def get_alphabet():
    alphabets_in_capital = []
    for i in range(ord('А'),ord('ѐ')):
        alphabets_in_capital.append(chr(i))
    return alphabets_in_capital

def encrypt_text(text, alphabet, encrypt_number):
    result = ''
    for char in text:
        if char in alphabet:
            for i in range(len(alphabet)):
                if(alphabet[i] == char):   
                    result += alphabet[i - encrypt_number]  
        else: result += char
    return result

def write_text_into_file(file_name, text):
    with open(file_name, 'w') as file:
        file.write(text)

def read_text_from_file(file_name):
    text = ''
    with open(file_name, 'r') as file:
        for line in file.readlines():
            text += line
    return text

def unencrypt_text(text, alphabet, encrypt_number):
    result = ''
    for char in text:
        if char in alphabet:
            for i in range(len(alphabet)):
                if(alphabet[i] == char):   
                    result += alphabet[i + encrypt_number]  
        else: result += char
    return result


    # Result:
    
# Get alphabet for text
alphabet = get_alphabet()
# Get normal text from file
normal_text = read_text_from_file('lesson_4/task_4_normal_text.txt')
# Encrypt text 
encrypted_text = encrypt_text(normal_text, alphabet, 2)
# Write encrypted text into file
write_text_into_file('lesson_4/task_4_encrypted_text.txt', encrypted_text)
# Get encrypted text from file
encrypted_text_from_file = read_text_from_file('lesson_4/task_4_encrypted_text.txt')
# unencrypt text
unencrypted_text = unencrypt_text(encrypted_text_from_file, alphabet, 2)


