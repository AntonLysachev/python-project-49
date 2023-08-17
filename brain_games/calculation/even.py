import random


def game():
    meaning = str(random.randint(1, 100))
    if int(meaning) % 2:
        correct = 'no'
    else:
        correct = 'yes'
    data = (meaning, correct)
    return data
