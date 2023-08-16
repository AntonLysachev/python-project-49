import random


def progression():
    rule = random.randint(2, 5)
    numb = random.randint(0, 9)
    start = random.randint(1, 100)
    prog = []
    r = range(10)
    for i in r:
        if i == 0:
            prog.append(i + start)
        else:
            prog.append(prog[i-1] + rule)
    result = prog[numb]
    prog[numb] = '..'
    meaning = ''
    for i in range(len(prog)):
        meaning += str(prog[i]) + ' '
    data = (meaning, str(result))
    return data
