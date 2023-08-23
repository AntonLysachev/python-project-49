import random


DESCRIPTION = 'What number is missing in the progression?'
SIZE_PROGRESSION = 10


def generate_progression():
    start = random.randint(1, 100)
    rule = random.randint(2, 5)
    progression = [start]
    for i in range(SIZE_PROGRESSION):
        progression.append(progression[i] + rule)
    return progression


def generate_round_data():
    progression = generate_progression()
    random_index = random.randint(0, SIZE_PROGRESSION - 1)
    right = progression[random_index]
    progression[random_index] = '..'
    question = ''
    for i in progression:
        question += str().join(f'{i} ')
    return question, str(right)
# не понял как тут использовать map
# question = map(str.join, progression)
# на выходе адрес обекта
# при конвертации list(map(str.join, progression))
# ошибка
# TypeError: descriptor 'join' for 'str' objects doesn't apply to a 'int' object
