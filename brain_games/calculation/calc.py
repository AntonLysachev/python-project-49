import random


def game():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    if (random.randint(1, 10)) % 2:
        result = num1 * num2
        meaning = f'{num1} * {num2}'
    else:
        result = num1 + num2
        meaning = f'{num1} + {num2}'
    data = (meaning, str(result))
    return data
