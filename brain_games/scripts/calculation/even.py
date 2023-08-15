import random


def even():
    meaning = str(random.randint(1, 100))
    if int(meaning) % 2:
        correct = 'no'
    else:
        correct = 'yes'
    data = (meaning, correct)
    return data