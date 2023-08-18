import random


description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def simple_or_not(numb):
    if numb == 1:
        return False
    for i in range(numb - 2):
        if not (numb % (i + 2)):
            return False
    return True


def play():
    number = random.randint(1, 100)
    right_answer = simple_or_not(number) and 'yes' or 'no'
    question = number
    data = (question, str(right_answer))
    return data
