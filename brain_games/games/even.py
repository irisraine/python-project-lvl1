from random import randint


GREET_MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'


# Единичный этап игры
def single_game_stage():
    NUMBER_LOWER_LIMIT = 1
    NUMBER_UPPER_LIMIT = 100

    question = randint(NUMBER_LOWER_LIMIT, NUMBER_UPPER_LIMIT)
    correct_answer = "yes" if is_even(question) else "no"
    return question, correct_answer


# Проверка числа на четность
def is_even(number):
    if number % 2 == 0:
        return True
