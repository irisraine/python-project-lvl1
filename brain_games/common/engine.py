import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def guessing_cycle(name, game_round):
    number_of_correct_answers = 0
    for _ in range(3):
        if (game_round()):
            number_of_correct_answers += 1
        else:
            print(f"Let's try again, {name}!")
            break

    if (number_of_correct_answers == 3):
        print(f"Congratulations, {name}!")


def is_correct_answer(answer, correct_answer):
    if (answer == correct_answer):
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(.", end=" ")
        print(f"Correct answer was '{correct_answer}'.")
