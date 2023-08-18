import prompt


def compare(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.description)
    for i in range(3):
        question, right_answer = game.play()
        print(f'Question: {question}')
        answ = prompt.string('Your answer: ')
        if answ == right_answer:
            print('Correct!')
            if i == 2:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{answ}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            break
