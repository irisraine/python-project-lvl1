from random import randint
import prompt


def guessing_even_number():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    number_of_correct_answers = 0

    for _ in range(3):
        current_quiz_number = randint(1, 100)
        print(f'Question: {current_quiz_number}')
        current_answer = prompt.string('Your answer: ')

        if (is_correct_answer(current_quiz_number, current_answer)):
            number_of_correct_answers += 1
        else:
            print(f"Let's try again, {name}!")
            break

    if (number_of_correct_answers == 3):
        print(f"Congratulations, {name}!")


def is_correct_answer(number, answer):
    if (number % 2 == 0):
        if (answer == 'yes'):
            print('Correct!')
            return True
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
    elif (number % 2 != 0):
        if (answer == 'no'):
            print('Correct!')
            return True
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
