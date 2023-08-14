import random
import prompt


def even():
    global meaning
    meaning = str(random.randint(1, 100))
    if int(meaning) % 2:
        return 'no'
    else:
        return 'yes'


def calc():
    global meaning
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    if (random.randint(1, 100)) % 2:
        result = num1 * num2
        meaning = f'{num1} * {num2}'
    else:
        result = num1 + num2
        meaning = f'{num1} + {num2}'
    return str(result)


def compare(name, switch):
      
    counter = 0
    while (counter < 3):
        if switch == 'e':
         game = even()
        elif switch == 'c':
            game = calc()
        question = game
        print(f'Question: {meaning}')
        answer = prompt.string('Your answer: ')
        if answer == question:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{question}'.")
            print(f"Let's try again, {name}!")
            break
        counter +=1
    if counter == 3:
        print(f'Congratulations, {name}!')