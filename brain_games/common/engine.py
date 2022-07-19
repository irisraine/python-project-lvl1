import prompt
import importlib


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def launch(game):
    username = welcome_user()
    game = f'brain_games.games.{game}'
    current_game = importlib.import_module(game)
    print(current_game.GREET_MESSAGE)
    guessing_loop(username, current_game.stage)


def ask_question(question):
    return (f'Question: {question}')


def guessing_loop(name, game_stage):
    number_of_correct_answers = 0
    for _ in range(3):
        question, correct_answer = game_stage()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if (is_correct_answer(answer, correct_answer)):
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
