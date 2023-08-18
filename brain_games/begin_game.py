import prompt


def play(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    ROUNDS = 3
    for i in range(ROUNDS):
        question, right = game.generate()
        print(f'Question: {question}')
        answ = prompt.string('Your answer: ')
        if answ != right:
            print(f"'{answ}' is wrong answer ;(. Correct answer was '{right}'.")
            print(f"Let's try again, {name}!")
            break
    else: 
        print('Correct!')
        if i == 2:
            print(f'Congratulations, {name}!')