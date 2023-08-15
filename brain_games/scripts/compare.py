import random
import prompt
from brain_games.calculation import even
from brain_games.calculation import calc
from brain_games.calculation import gcd
from brain_games.calculation import progression
from brain_games.calculation import prime


def compare(name, switch):
    counter = 0
    while (counter < 3):
        if switch == 'evn':
            game = even.even()
        elif switch == 'cac':
            game = calc.calc()
        elif switch == 'gcd':
            game = gcd.gcd()
        elif switch == 'prn':
            game = progression.progression()
        elif switch == 'pre':
            game = prime.prime()
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
