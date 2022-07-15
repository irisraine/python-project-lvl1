from brain_games.common.engine import is_correct_answer
from random import randint
import prompt


GREET_MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'


def stage():
    current_number = randint(1, 100)
    print(f'Question: {current_number}')
    current_answer = prompt.string('Your answer: ')
    current_correct_answer = "yes" if (current_number % 2 == 0) else "no"
    return is_correct_answer(current_answer, current_correct_answer)
