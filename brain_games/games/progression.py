import random
from brain_games import constant


DESCRIPTION = 'What number is missing in the progression?'


def generate_progression():
    progression = []
    start = random.randint(1, 100)
    rule = random.randint(2, 5)
    for i in range(constant.SIZE):
        if i == 0:
            progression.append(i + start)
        else:
            progression.append(progression[i - 1] + rule)
    return progression


def generate_round_data():
    progression = generate_progression()
    random_index = random.randint(0, constant.SIZE - 1)
    right = progression[random_index]
    progression[random_index] = '..'
    question = ''
    for i in progression:               # не понял как тут использовать map
        question += str().join(f'{i} ')  # question = map(str.join, progression)
    return question, str(right)         # на выходе адрес обекта
