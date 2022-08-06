from random import randint


GREET_MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'

NUMBER_LOWER_LIMIT, NUMBER_UPPER_LIMIT = 1, 100


def single_game_stage():
    """Logic of singular 'Is even' game stage"""
    question = randint(NUMBER_LOWER_LIMIT, NUMBER_UPPER_LIMIT)
    correct_answer = "yes" if is_even(question) else "no"

    return str(question), correct_answer


def is_even(number):
    """Check number is even or odd"""
    return number % 2 == 0
