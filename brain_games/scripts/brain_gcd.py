#!/usr/bin/env python3
from brain_games import begin_game
from brain_games.games import gcd


def game():
    begin_game.play(gcd)


def main():
    game()


if __name__ == '__main__':
    main()
