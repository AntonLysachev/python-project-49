import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def simple_or_not(numb):
    if numb == 1:
        return False
    for i in range(2, int(numb ** 0.5 + 1)):
        if not (numb % (i + 2)):
            return False
    return True


def generate():
    number = random.randint(1, 100)
    right = simple_or_not(number) and 'yes' or 'no'
    question = number
    data = (question, str(right))
    return data
