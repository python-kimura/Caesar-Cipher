whats_direction = input('Что нужно сделать: шифровать или дешифровать? \n').lower()
while whats_direction != 'шифровать' and whats_direction != 'дешифровать':
    whats_direction = input('Неверный ввод. Напишите "шифровать" либо "дешифровать". \n').lower()

whats_language = input('Какой нужен язык: русский или английский? \n').lower()
while whats_language != 'русский' and whats_language != 'английский':
    whats_language = input('Неверный ввод. Напишите "русский" либо "английский". \n').lower()

whats_step = input('Чему равен сдвиг буквы по алфавиту? Ответ напишите числом. \n')
while whats_step.isdigit() != True:
    whats_step = input('Неверный ввод. Напишите число. \n')

whats_text = input('Какой текст нужно использовать сейчас? \n')
while whats_text.isspace() == True:
    whats_text = input('Неверный ввод. Введите текст. \n')


def caesar(direction, language, step, text):

    upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

    for i in range(len(text)):

        if language == 'русский':
            alphas = 32
            low_alphabet = lower_rus_alphabet
            upp_alphabet = upper_rus_alphabet
        if language == 'английский':
            alphas = 26
            low_alphabet = lower_eng_alphabet
            upp_alphabet = upper_eng_alphabet


        if text[i].isalpha():

            if text[i] == text[i].lower():
                place = low_alphabet.index(text[i])
            if text[i] == text[i].upper():
                place = upp_alphabet.index(text[i])

            if direction == 'дешифровать':
                index = (place - int(step)) % alphas

            elif direction == 'шифровать':
                index = (place + int(step)) % alphas

            if text[i] == text[i].lower():
                print(low_alphabet[index], end='')
            if text[i] == text[i].upper():
                print(upp_alphabet[index], end='')            

        else:
            print(text[i], end='')
        
caesar(whats_direction, whats_language, whats_step, whats_text)