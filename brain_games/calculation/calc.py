import random


def game():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    choice = random.randint(1,9) % 3
    match choice:
        case 0:
            result = num1 * num2
            meaning = f'{num1} * {num2}'
        case 1:
            result = num1 - num2
            meaning = f'{num1} - {num2}'
        case 2:
            result = num1 + num2
            meaning = f'{num1} + {num2}'
    data = (meaning, str(result))
    return data
