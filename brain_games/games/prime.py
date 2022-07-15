from random import randint
from brain_games.common.engine import is_correct_answer
import prompt


GREET_MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def stage():
    current_number = randint(1, 100)
    print(f'Question: {current_number}')
    current_answer = prompt.string('Your answer: ')
    current_correct_answer = "yes" if (is_prime(current_number)) else "no"
    return is_correct_answer(current_answer, current_correct_answer)


def is_prime(number):
    for i in range(2, number):
        if (number % i == 0):
            return False
    return True
