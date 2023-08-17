import math
import random


def game():
    while (1):
        a = random.randint(1, 100)
        if a % 2:
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
