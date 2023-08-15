from brain_games import cli


def greetings():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    return name
