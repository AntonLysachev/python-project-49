import math
import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'

# использую (random.randrange) для приведения числа к четному значению
# если использовать нечетные числа ответ почти всегда 1


def generate():
    number_a = random.randrange(2, 100, 2)
    number_b = random.randrange(2, 100, 2)
    right = math.gcd(number_a, number_b)
    question = f'{number_a} {number_b}'
    data = (question, str(right))
    return data
