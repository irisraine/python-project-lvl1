from brain_games.verification.is_correct import is_correct_answer
from random import randint
import prompt


def even_stage():
    current_number = randint(1, 100)
    print(f'Question: {current_number}')
    current_answer = prompt.string('Your answer: ')
    current_correct_answer = "yes" if (current_number % 2 == 0) else "no"
    if (is_correct_answer(current_answer, current_correct_answer)):
        return True
