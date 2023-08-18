import math
import random


description = 'Find the greatest common divisor of given numbers.'


def play():
    while (1):                      # Здесь я привожу значения к четному числу
        a = random.randint(1, 100)  # С нечетными числами ответ почти всегда - 1
        if a % 2:                   # Так игра немного интереснее
            continue
        else:
            break
    while (1):
        b = random.randint(1, 100)
        if b % 2:
            continue
        else:
            break

    right_answer = math.gcd(a, b)
    question = f'{a} {b}'
    data = (question, str(right_answer))
    return data
