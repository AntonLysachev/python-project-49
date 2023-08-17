#!/usr/bin/env python3
from brain_games import engine
from brain_games.calculation import progression


def game():
    print('What number is missing in the progression?')
    engine.compare(progression)


def main():
    game()


if __name__ == '__main__':
    main()
