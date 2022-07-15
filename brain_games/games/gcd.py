from random import randint
from brain_games.common.engine import is_correct_answer
import prompt


GREET_MESSAGE = 'Find the greatest common divisor of given numbers.'


def stage():
    first_number, second_number = randint(1, 100), randint(1, 100)
    print(f'Question: {first_number} {second_number}')
    answer = prompt.string('Your answer: ')
    correct_answer = gcd(first_number, second_number)
    return is_correct_answer(answer, str(correct_answer))


def gcd(number_one, number_two):
    number_remainder = max(number_one, number_two) % min(number_one, number_two)

    if (number_remainder == 0):
        return min(number_one, number_two)
    else:
        number_one = min(number_one, number_two)
        number_two = number_remainder
        return gcd(number_one, number_two)
