import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate():
    question = str(random.randint(1, 100))
    right = int(question) % 2 and 'no' or 'yes'
    data = (question, right)
    return data
