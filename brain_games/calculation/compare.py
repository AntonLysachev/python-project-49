import prompt
from brain_games.calculation import even
from brain_games.calculation import calc
from brain_games.calculation import gcd
from brain_games.calculation import progression
from brain_games.calculation import prime


def switch(swc):
    if swc == 'evn':
        return even.even()
    elif swc == 'cac':
        return calc.calc()
    elif swc == 'gcd':
        return gcd.gcd()
    elif swc == 'prn':
        return progression.progression()
    elif swc == 'pre':
        return prime.prime()


def compare(name, swch):
    counter = 0
    while (counter < 3):
        game = switch(swch)
        quest = game[1]
        meaning = game[0]
        print(f'Question: {meaning}')
        answ = prompt.string('Your answer: ')
        if answ == quest:
            print('Correct!')
        else:
            print(f"'{answ}' is wrong answer ;(. Correct answer was '{quest}'.")
            print(f"Let's try again, {name}!")
            break
        counter += 1
    if counter == 3:
        print(f'Congratulations, {name}!')
