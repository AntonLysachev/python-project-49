#!/usr/bin/env python3
from brain_games import engine
from brain_games.calculation import prime


def game():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    engine.compare(prime)


def main():
    game()


if __name__ == '__main__':
    main()
