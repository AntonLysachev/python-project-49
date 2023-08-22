import math
import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_round_data():
    number_a = random.randint(1, 100)
    number_b = random.randint(1, 100)
    right = math.gcd(number_a, number_b)
    question = f'{number_a} {number_b}'
    return question, str(right)
