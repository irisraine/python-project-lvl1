from random import randint


GREET_MESSAGE = 'Find the greatest common divisor of given numbers.'


# Единичный этап игры
def single_game_stage():
    NUMBER_LOWER_LIMIT = 1
    NUMBER_UPPER_LIMIT = 100

    first_number = randint(NUMBER_LOWER_LIMIT, NUMBER_UPPER_LIMIT)
    second_number = randint(NUMBER_LOWER_LIMIT, NUMBER_UPPER_LIMIT)
    question = f'{first_number} {second_number}'
    correct_answer = gcd(first_number, second_number)
    return question, str(correct_answer)


# Получение наибольшего общего делителя числа
def gcd(number_one, number_two):
    number_remainder = max(number_one, number_two) % min(number_one, number_two)
    if number_remainder == 0:
        return min(number_one, number_two)
    else:
        return gcd(min(number_one, number_two), number_remainder)
