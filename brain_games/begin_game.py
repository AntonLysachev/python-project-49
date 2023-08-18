import prompt

# решил приветствие вынести в отдельную функцию
# на мой взгляд так понятнее за что отвечает каждый блок кода


def greetings(description):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(description.DESCRIPTION)
    return name


def play(game):
    user = greetings(game)
    ROUNDS = 3
    for i in range(ROUNDS):
        question, right = game.generate()
        print(f'Question: {question}')
        answ = prompt.string('Your answer: ')
        if answ != right:
            print(f"'{answ}' is wrong answer ;(. Correct answer was '{right}'.")
            print(f"Let's try again, {user}!")
            break
        print('Correct!')
    else:
        print(f'Congratulations, {user}!')
