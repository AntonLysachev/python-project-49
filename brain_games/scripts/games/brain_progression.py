#!/usr/bin/env python3
from brain_games import compare
from brain_games import greetings


def game():
    name = greetings.greetings()
    print('What number is missing in the progression?')
    compare.compare(name, 'prn')


def main():
    game()


if __name__ == '__main__':
    main()
