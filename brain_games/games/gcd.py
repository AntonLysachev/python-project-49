import math
import random


description = 'Find the greatest common divisor of given numbers.'


def generate():
    number_a = random.randrange(2, 100, 2)  # использую (random.randrange) для приведения числа к четному значению
    number_b = random.randrange(2, 100, 2)  # если использовать нечетные числа ответ почти всегда 1
    right = math.gcd(number_a, number_b)
    question = f'{number_a} {number_b}'
    data = (question, str(right))
    return data
