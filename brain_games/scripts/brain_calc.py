#!/usr/bin/env python3
from brain_games import game_engine
from brain_games.games import calc


def game():
    game_engine.play(calc)


def main():
    game()


if __name__ == '__main__':
    main()
