import random

DESCRIPTION = 'What is the result of the expression?'


def generate():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice('+-*')
    match operator:
        case '*':
            right = num1 * num2
            question = f'{num1} * {num2}'
        case '-':
            right = num1 - num2
            question = f'{num1} - {num2}'
        case '+':
            right = num1 + num2
            question = f'{num1} + {num2}'
    data = (question, str(right))
    return data
