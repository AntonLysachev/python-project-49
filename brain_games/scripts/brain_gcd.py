#!/usr/bin/env python3
from brain_games import engine
from brain_games.calculation import gcd


def game():
    print('Find the greatest common divisor of given numbers.')
    engine.compare(gcd)


def main():
    game()


if __name__ == '__main__':
    main()
