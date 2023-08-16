#!/usr/bin/env python3
from brain_games.calculation import compare
from brain_games import greetings


def game():
    name = greetings.greetings()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    compare.compare(name, 'evn')


def main():
    game()


if __name__ == '__main__':
    main()
