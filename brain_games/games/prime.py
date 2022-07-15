from random import randint
from brain_games.verification.is_correct import is_correct_answer
import prompt


def prime_stage():
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
