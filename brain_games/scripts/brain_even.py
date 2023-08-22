#!/usr/bin/env python3
from brain_games import game_engine
from brain_games.games import even


def game():
    game_engine.play(even)


def main():
    game()


if __name__ == '__main__':
    main()
