def compare(name, answer, question):
    if answer == question:
        print('Correct!')
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{question}'.")
        print(f"Let's try again, {name}!")
        return 1
