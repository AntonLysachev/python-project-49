import random


description = 'Answer "yes" if the number is even, otherwise answer "no".'


def play():
    question = str(random.randint(1, 100))
    right_answer = int(question) % 2 and 'no' or 'yes'
    data = (question, right_answer)
    return data
