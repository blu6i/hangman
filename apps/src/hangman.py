# Добавить список с угаданными буквами +
# Добавить список с угаданными словами +
# Сделать возможноть выигрывать с полным вводом словом +
# Спрашивать пользователя об продолжении игры +
# Добавить возможность при повторном вводе слова корректно вводить буквы+
# Сделать выбор тематики
# Сделать несколько списков со словами разной тематики
# Добавить выбор уровня сложности: low, middle, hard
# low - пишется тема слова, открываются первая и последняя буква
# middle - открываются первая и последняя буква
# hard - открывается тема слова
# hard+ - ничего не открывается

import os
import random


# *********************************
# *** Генераторы разных списков ***
# *********************************

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
        # голова, торс, обе руки, одна нога
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
        # голова, торс, обе руки
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
        # голова, торс и одна рука
        '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
        # голова и торс
        '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
        # голова
        '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
        # начальное состояние
        '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    print(stages[tries])


# Генератор русского алфавита
def is_ru_alph():
    return [chr(i) for i in range(ord('а'), ord('я') + 1)]


# ****************************************************************************************************
# *** Блок определяет введена слово или букву, также првоеряет на корректность ввода буквы и слова ***
# ****************************************************************************************************

# Валидатор слова
def is_valid_word(word):
    for i in word:
        if i not in is_ru_alph():
            return False
    return True


# Валидатор символа
def is_valid_letter(letter):
    if letter.isalpha() and letter in is_ru_alph():
        return True
    return False


# Проверка что вводится (Слово или буква)
def is_word_or_letter(chw, word_list, letter_list):
    if len(chw) == 1:
        if is_valid_letter(chw):
            if chw not in letter_list:
                return chw
            else:
                return is_word_or_letter(input('Вы уже вводили такую букву ранее, введите другую букву\n<< '),
                                         word_list, letter_list)
        else:
            return is_word_or_letter(input('Вы ввели не букву, введите букву\n<< '),
                                     word_list, letter_list)
    else:
        if is_valid_word(chw):
            if chw not in word_list:
                return chw
            else:
                return is_word_or_letter(input('Вы уже вводили такое слово ранее, введите другое слово\n<< '),
                                         word_list, letter_list)
        else:
            return is_word_or_letter(input('В слове содержатся другие знаки, введите слово\n<< '),
                                     word_list, letter_list)


# ***************************************************************
# *** Блок для заполнения начальных данных (Слово, сложность) ***
# ***************************************************************

# Список слов
def get_word(topic):
    rand_word = ''
    if topic == 'еда':
        with open("eat.txt", encoding='UTF-8') as file:
            word_list = file.read().split()
        rand_word = random.sample(word_list, 1)
    elif topic == 'транспорт':
        with open("ts.txt", encoding='UTF-8') as file:
            word_list = file.read().split()
        rand_word = random.sample(word_list, 1)
    elif topic == 'города':
        with open("state.txt", encoding='UTF-8') as file:
            word_list = file.read().split()
        rand_word = random.sample(word_list, 1)
    elif topic == 'страны':
        with open("lands.txt", encoding='UTF-8') as file:
            word_list = file.read().split()
        rand_word = random.sample(word_list, 1)
    elif topic == 'уроки':
        with open("lern.txt", encoding='UTF-8') as file:
            word_list = file.read().split()
        rand_word = random.sample(word_list, 1)
    elif topic == 'соц. сети (название)':
        with open("social.txt", encoding='UTF-8') as file:
            word_list = file.read().split()
        rand_word = random.sample(word_list, 1)
    return ''.join(rand_word)


def is_start_infobar(difficulty, topic, word):
    # └┐┘┌│─
    answer_word = [list(word)[0]] + ['-'] * (len(word) - 2) + [list(word)[len(word) - 1]]
    answer_word = ''.join(answer_word)
    if difficulty == 'Легкая':
        print('┌────────────────────────────────────────────────────────\n'
              f'│\tСложность: {difficulty}\n'
              f'│\tТема: {topic}\n'
              f'│\tСлово: {answer_word}\n'
              f'└────────────────────────────────────────────────────────')
    elif difficulty == 'Средняя':
        print('┌────────────────────────────────────────────────────────\n'
              f'│\tСложность: {difficulty}\n'
              f'│\tТема: {topic}\n'
              f'└────────────────────────────────────────────────────────')
    elif difficulty == 'Сложная':
        print('┌────────────────────────────────────────────────────────\n'
              f'│\tСложность: {difficulty}\n'
              f'│\tТема: {topic}\n'
              f'└────────────────────────────────────────────────────────')
    else:
        print('Ошибка infobar#1')


def is_game_infobar(word, tries, guessed_word, guessed_letter, flag, topic):
    # └┐┘┌│─
    display_hangman(tries)
    st_list = ['мимо', 'почти', 'ой-ой мимо', 'не так', 'не то']
    g_list = ['правильно', 'угадал', 'в точку']
    if not flag:
        print(f'┌────────────────────────────────────────────────────────\n'
              f'│\t {''.join(random.sample(st_list, 1))}\n'
              f'│\t Слово: {word}\n'
              f'│\t Тема: {topic}\n'
              f'│\t Жизни: {tries}\n'
              f'│\t Использованы слова: {' | '.join(guessed_word)}\n'
              f'│\t Использованы буквы: {' | '.join(guessed_letter)}\n'
              f'└────────────────────────────────────────────────────────')
    else:
        print(f'┌────────────────────────────────────────────────────────\n'
              f'│\t {''.join(random.sample(g_list, 1))}\n'
              f'│\t Слово: {word}\n'
              f'│\t Тема: {topic}\n'
              f'│\t Жизни: {tries}\n'
              f'│\t Использованы слова: {' | '.join(guessed_word)}\n'
              f'│\t Использованы буквы: {' | '.join(guessed_letter)}\n'
              f'└────────────────────────────────────────────────────────')


# *************************************************************************
# *** Блок валлидаторов ввода ответа пользователя на игровые условности ***
# *************************************************************************

# Валидатор выбора ответа на продолжение игры
def is_valid_next_trie(choice):
    if choice in 'ny':
        return choice
    return is_valid_next_trie(input('Введите корректный ответ (y - да, n - нет)'))


def is_valid_topic(topic, difficulty):
    topic_list = ['еда', 'транспорт', 'города', 'страны', 'уроки', 'соц. сети (название)']
    if not topic.isdigit():
        return is_valid_topic(input('Не корректный ввод, повторите ввод\n<< '), difficulty)
    topic = int(topic)
    if topic in range(1, len(topic_list) + 1):
        return topic_list[int(topic) - 1]
    return is_valid_topic(input('Не корректный ввод, повторите ввод\n<< '), difficulty)


def is_valid_difficulty(difficulty):
    difficulty_list = ['Легкая', 'Средняя', 'Сложная']
    if not difficulty.isdigit():
        return is_valid_difficulty(input('Сложность указана не правильно. Введите цифру сложности\n<< '))
    if difficulty in '1 2 3':
        return difficulty_list[int(difficulty) - 1]
    return is_valid_difficulty(input('Сложность указана не правильно. Введите цифру сложности\n<< '))


# ********************************
# *** Блок с телом самой игрой ***
# ********************************
def play(orig_word, word, copy_word):  # Оригинальное слово, слово с тире
    word = list(word)
    answer_word = list(copy_word)
    tries = 6
    count_tries = 0
    guessed_word = []
    guessed_letter = []
    flag = True
    # is_game_infobar(''.join(answer_word).upper(), tries, guessed_word, guessed_letter)
    while '-' in answer_word and tries != 0:
        print('\n')
        letter_word = is_word_or_letter(input('Введите букву или слово полностью\n<< '), guessed_word, guessed_letter)
        if len(letter_word) == 1:
            guessed_letter.append(letter_word)
            if letter_word in word:
                while letter_word in word:
                    answer_word[word.index(letter_word)] = word[word.index(letter_word)]
                    word[word.index(letter_word)] = '-'
                print('Буква угадана')
                count_tries += 1
            else:
                tries -= 1
                count_tries += 1
                flag = False
        else:
            guessed_word.append(letter_word)
            if letter_word == orig_word:
                count_tries += 1
                break
            else:
                tries -= 1
                count_tries += 1
                flag = False
        is_game_infobar(''.join(answer_word).upper(), tries, guessed_word, guessed_letter, flag, topic)
    if tries != 0:
        print(f'Вы угадали слово {orig_word.upper()}. За {count_tries} попыток')
    else:
        print(f'Вы проиграли! Было загадано слово: {orig_word.upper()}')


os.chdir('../word_list')
while True:
    count_word = 0
    topic_list = ['еда', 'транспорт', 'города', 'страны', 'уроки', 'соц. сети (название)']
    text_for_topic = ('Темы слов\n'
                      '1) Еда\n'
                      '2) Транспорт\n'
                      '3) Города\n'
                      '4) Страны\n'
                      '5) Уроки\n'
                      '6) Соц. сети (название)\n'
                      'Введите цифру темы\n<< ')
    text_for_difficulty = ('Выберите сложность\n'
                           '1) Легкая (Выбор темы, открывается первая и последняя буква)\n'
                           '2) Средняя (Выбор темы, не открываются буквы)\n'
                           '3) Сложная (Нет выбора темы, не открываются буквы)\n'
                           'Введите цифру сложности:\n<< ')
    difficulty = is_valid_difficulty(input(text_for_difficulty))  # Выбор сложности
    if difficulty != 'Сложная':
        topic = is_valid_topic(input(text_for_topic), difficulty)  # Выбор темы
    else:
        topic = ''.join(random.sample(topic_list, 1))
    hidden_word = get_word(topic)  # Получение загадонного слова по выбранной теме
    copy_hidden_word = hidden_word  # Копия слова для первого и послнеднего символа
    word = hidden_word  # Копия оригинального слова
    if difficulty == 'Легкая':
        # Конструктора слова для легково режима, заменяет все буквы кроме послдней и первой
        copy_hidden_word = ''.join(
            [list(hidden_word)[0]] + ['-'] * (len(hidden_word) - 2) + [list(hidden_word)[len(hidden_word) - 1]])
        hidden_word = '-' + hidden_word[1:len(hidden_word) - 1] + '-'  # Замена певрой и последней буквы на "-"
    else:
        copy_hidden_word = '-' * len(hidden_word)  # Конструктор слова для других режимов
    is_start_infobar(difficulty, topic, word)  # Информация о выбранной теме, сложности
    play(word, hidden_word, copy_hidden_word)
    next_trie = is_valid_next_trie(input('Продолжить? (y - да|n - нет) '))
    if next_trie == 'n':
        print('Вы завершили игру')
        break
