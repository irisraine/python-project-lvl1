from random import randint
from brain_games.common.engine import is_correct_answer
import prompt


GREET_MESSAGE = 'What is the result of the expression?'


def stage():
    arithmetic_operations = ['+', '-', '*']
    current_first_number, current_second_number = randint(1, 100), randint(1, 100)
    current_arithmetic_operation = arithmetic_operations[randint(0, 2)]
    current_expression = f'{current_first_number} {current_arithmetic_operation} {current_second_number}'
    print(f'Question: {current_expression}')

    if (current_arithmetic_operation == "+"):
        current_correct_answer = current_first_number + current_second_number
    elif (current_arithmetic_operation == "-"):
        current_correct_answer = current_first_number - current_second_number
    elif (current_arithmetic_operation == "*"):
        current_correct_answer = current_first_number * current_second_number

    current_answer = prompt.string('Your answer: ')
    return is_correct_answer(current_answer, str(current_correct_answer))
