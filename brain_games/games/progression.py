import random


description = 'What number is missing in the progression?'


def generator():
    prog = []
    start = random.randint(1, 100)
    rule = random.randint(2, 5)
    size = 10
    for i in range(size):
        if i == 0:
            prog.append(i + start)
        else:
            prog.append(prog[i - 1] + rule)
    return prog


def generate():
    numb = random.randint(0, 9)
    progression = generator()
    right = progression[numb]
    progression[numb] = '..'
    question = ''
    for i in range(len(progression)):
        question += str(progression[i]) + ' '
    data = (question, str(right))
    return data
