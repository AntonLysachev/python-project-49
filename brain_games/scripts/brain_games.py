#!/usr/bin/env python3
from brain_games import cli


def greetings():
    print('Welcome to the Brain Games!')
    cli.welcome_user()


def main():
    greetings()


if __name__ == '__main__':
    main()
