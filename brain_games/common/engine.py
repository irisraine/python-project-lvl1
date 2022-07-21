import prompt


NUMBER_OF_STAGES = 3


def launch(game):
    """ Запуск полного игрового цикла."""
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(game.GREET_MESSAGE)

    for _ in range(NUMBER_OF_STAGES):
        question, correct_answer = game.single_game_stage()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.", end=" ")
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return None

    print(f"Congratulations, {name}!")
