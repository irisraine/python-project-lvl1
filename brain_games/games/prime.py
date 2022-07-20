from random import randint


GREET_MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# Единичный этап игры
def single_game_stage():
    NUMBER_LOWER_LIMIT = 1
    NUMBER_UPPER_LIMIT = 100

    question = randint(NUMBER_LOWER_LIMIT, NUMBER_UPPER_LIMIT)
    correct_answer = "yes" if is_prime(question) else "no"
    return question, correct_answer


# Проверка числа на простоту
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if (number % i == 0):
            return False
    return True
