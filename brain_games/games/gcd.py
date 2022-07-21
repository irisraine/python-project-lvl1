from random import randint


GREET_MESSAGE = 'Find the greatest common divisor of given numbers.'

NUMBER_LOWER_LIMIT, NUMBER_UPPER_LIMIT = 1, 100


def single_game_stage():
    """Единичный этап игры."""
    first_number = randint(NUMBER_LOWER_LIMIT, NUMBER_UPPER_LIMIT)
    second_number = randint(NUMBER_LOWER_LIMIT, NUMBER_UPPER_LIMIT)
    question = f'{first_number} {second_number}'
    correct_answer = gcd(first_number, second_number)

    return question, str(correct_answer)


def gcd(number_one, number_two):
    """Получение наибольшего общего делителя числа."""
    number_remainder = max(number_one, number_two) % min(number_one, number_two)

    if number_remainder == 0:
        return min(number_one, number_two)
    else:
        return gcd(min(number_one, number_two), number_remainder)
