#!/usr/bin/env python3
import prompt
import random
from brain_games import cli


def greetings():
    print('Welcome to the Brain Games!')


def game():
    counter = 0
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while (counter < 3):
        numb = random.randint(0, 100)
        print(f'Question: {numb}')
        answer = prompt.string('Your answer: ')
        if numb % 2:
            if answer == 'no':
                print('Correct!')
                counter += 1
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again, {name}!")
                break
        elif answer == 'yes':
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            break
    if counter == 3:
        print(f'Congratulations, {name}!')


def main():
    greetings()
    game()


if __name__ == '__main__':
    main()
