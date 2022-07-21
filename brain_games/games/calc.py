from random import randint


GREET_MESSAGE = 'What is the result of the expression?'

NUMBER_LOWER_LIMIT, NUMBER_UPPER_LIMIT = 1, 100


def single_game_stage():
    """Единичный этап игры."""
    arithmetic_operations = ['+', '-', '*']
    first_number = randint(NUMBER_LOWER_LIMIT, NUMBER_UPPER_LIMIT)
    second_number = randint(NUMBER_LOWER_LIMIT, NUMBER_UPPER_LIMIT)
    arithmetic_operation = arithmetic_operations[randint(0, 2)]
    question = f'{first_number} {arithmetic_operation} {second_number}'

    if arithmetic_operation == "+":
        correct_answer = first_number + second_number
    elif arithmetic_operation == "-":
        correct_answer = first_number - second_number
    elif arithmetic_operation == "*":
        correct_answer = first_number * second_number

    return question, str(correct_answer)
