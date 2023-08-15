#!/usr/bin/env python3
from brain_games import compare
from brain_games import greetings


def game():
    name = greetings.greetings()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    compare.compare(name, 'pre')


def main():
    game()


if __name__ == '__main__':
    main()
