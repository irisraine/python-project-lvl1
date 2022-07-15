from random import randint
from brain_games.common.engine import is_correct_answer
import prompt


GREET_MESSAGE = 'Find the greatest common divisor of given numbers.'


def stage():
    current_first_number, current_second_number = randint(1, 100), randint(1, 100)
    print(f'Question: {current_first_number} {current_second_number}')
    current_answer = prompt.string('Your answer: ')
    current_correct_answer = gcd(current_first_number, current_second_number)
    return is_correct_answer(current_answer, str(current_correct_answer))


def gcd(number_one, number_two):
    number_remainder = max(number_one, number_two) % min(number_one, number_two)

    if (number_remainder == 0):
        return min(number_one, number_two)
    else:
        number_one = min(number_one, number_two)
        number_two = number_remainder
        return gcd(number_one, number_two)
