#!/usr/bin/env python3
from brain_games.scripts import compare
from brain_games import cli



def greetings():
    print('Welcome to the Brain Games!')


def game():
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    compare.compare(name, 'e')
    

def main():
    greetings()
    game()


if __name__ == '__main__':
    main()
