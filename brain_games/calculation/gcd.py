import math
import random


def gcd():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    result = math.gcd(a, b)
    meaning = f'{a} {b}'
    data = (meaning, str(result))
    return data