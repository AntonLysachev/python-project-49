import prompt


print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print(f'Hello, {name}!')

def compare(game):
    counter = 0
    while (counter < 3):
        play=game.game()
        quest = play[1]
        meaning = play[0]
        print(f'Question: {meaning}')
        answ = prompt.string('Your answer: ')
        if answ == quest:
            print('Correct!')
        else:
            print(f"'{answ}' is wrong answer ;(. Correct answer was '{quest}'.")
            print(f"Let's try again, {name}!")
            break
        counter += 1
    if counter == 3:
        print(f'Congratulations, {name}!')
