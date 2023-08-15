#!/usr/bin/env python3
from brain_games import compare
from brain_games import greetings


def game():
    name = greetings.greetings()
    print('Find the greatest common divisor of given numbers.')
    compare.compare(name, 'gcd')


def main():
    game()


if __name__ == '__main__':
    main()
