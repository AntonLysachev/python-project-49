#!/usr/bin/env python3
from brain_games import engine
from brain_games.calculation import even


def game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    engine.compare(even)


def main():
    game()


if __name__ == '__main__':
    main()
