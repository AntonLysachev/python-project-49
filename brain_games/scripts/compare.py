import random
import prompt
from brain_games.calculation import even
from brain_games.calculation import calc


def gcd():
    global meaning
    
    return str(result)


def compare(name, switch):
    counter = 0
    while (counter < 3):
        if switch == 'e':
            game = even.even()
        elif switch == 'c':
            game = calc.calc()
        question = game[1]
        meaning = game[0]
        print(f'Question: {meaning}')
        answer = prompt.string('Your answer: ')
        if answer == question:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{question}'.")
            print(f"Let's try again, {name}!")
            break
        counter += 1
    if counter == 3:
        print(f'Congratulations, {name}!')
