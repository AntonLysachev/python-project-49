#!/usr/bin/env python3
from brain_games import compare
from brain_games import greetings


def game():
    name = greetings.greetings()
    print('What is the result of the expression?')
    compare.compare(name, 'cac')


def main():
    game()


if __name__ == '__main__':
    main()
