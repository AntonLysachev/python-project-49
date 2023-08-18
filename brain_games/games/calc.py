import random

DESCRIPTION = 'What is the result of the expression?'


def generate():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    choice = random.randint(1, 9) % 3
    match choice:
        case 0:
            right = num1 * num2
            question = f'{num1} * {num2}'
        case 1:
            right = num1 - num2
            question = f'{num1} - {num2}'
        case 2:
            right = num1 + num2
            question = f'{num1} + {num2}'
    data = (question, str(right))
    return data
