import math
import random


description = 'Find the greatest common divisor of given numbers.'


def get_even_number():
    while (1):
        namber = random.randint(1, 100)
        if namber % 2:
            continue
        else:
            return namber


def play():
    number_a = get_even_number()
    number_b = get_even_number()
    right = math.gcd(number_a, number_b)
    question = f'{number_a} {number_b}'
    data = (question, str(right))
    return data
