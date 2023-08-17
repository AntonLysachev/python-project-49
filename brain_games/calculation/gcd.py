import math
import random


def game():
    while (1):                      #Здесь я привозу значения к четному чисту
        a = random.randint(1, 100)  #С нечетными чистали ответ почти всегда - 1
        if a % 2:                   #Так игра немного интереснее
            continue
        else:
            break
    while (1):
        b = random.randint(1, 100)
        if b % 2:
            continue
        else:
            break

    result = math.gcd(a, b)
    meaning = f'{a} {b}'
    data = (meaning, str(result))
    return data
