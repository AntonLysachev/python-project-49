#!/usr/bin/env python3
from brain_games import engine
from brain_games.calculation import calc


def game():
    print('What is the result of the expression?')
    engine.compare(calc)


def main():
    game()


if __name__ == '__main__':
    main()
