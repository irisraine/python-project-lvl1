from random import randint


GREET_MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'

NUMBER_LOWER_LIMIT, NUMBER_UPPER_LIMIT = 1, 250


def single_game_stage():
    """Единичный этап игры."""
    question = randint(NUMBER_LOWER_LIMIT, NUMBER_UPPER_LIMIT)
    correct_answer = "yes" if is_prime(question) else "no"

    return str(question), correct_answer


def is_prime(number):
    """Проверка числа на простоту."""
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
