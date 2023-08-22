#!/usr/bin/env python3
from brain_games import game_engine
from brain_games.games import prime


def game():
    game_engine.play(prime)


def main():
    game()


if __name__ == '__main__':
    main()
