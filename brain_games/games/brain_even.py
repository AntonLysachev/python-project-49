#!/usr/bin/env python3
from brain_games.scripts import compare
from brain_games import cli
import random
import prompt


def greetings():
    print('Welcome to the Brain Games!')


def game():
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while (counter < 3):
        numb = random.randint(1, 100)
        print(f'Question: {numb}')
        answer = prompt.string('Your answer: ')
        if numb % 2:
            question = 'no'
        else:
            question = 'yes'
        if compare.compare(name,answer, question):
            break
        counter += 1
    if counter == 3:
        print(f'Congratulations, {name}!')


def main():
    greetings()
    game()


if __name__ == '__main__':
    main()
