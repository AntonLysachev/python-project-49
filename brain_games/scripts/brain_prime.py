#!/usr/bin/env python3
from brain_games import begin_game
from brain_games.games import prime


def game():
    begin_game.compare(prime)


def main():
    game()


if __name__ == '__main__':
    main()
