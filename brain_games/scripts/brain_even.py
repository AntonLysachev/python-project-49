#!/usr/bin/env python3
import prompt
import random
import sys
sys.path.append('d:\\Github\\python-project-49\\brain_games')
import cli


def greetings():
    print('Welcome to the Brain Games!')


def game():
    counter = 0
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while(counter < 3):
        numb = random.randint(0, 100)
        print(f'Question: {numb}')
        answer = prompt.string('Your answer: ')
        if numb%2:
            if answer == 'no':
                print('Correct!')
                counter += 1
            else:
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again, {name}!")
                break
        elif answer == 'yes':
            print('Correct!')
            counter += 1
        else:
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            break
    print(f'Congratulations, {name}!')

def main():
    greetings()
    game()


if __name__ == '__main__':
    main()
