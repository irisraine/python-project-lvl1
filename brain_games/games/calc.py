from random import randint
from brain_games.common.engine import is_correct_answer
import prompt


GREET_MESSAGE = 'What is the result of the expression?'


def stage():
    arithmetic_operations = ['+', '-', '*']
    first_number, second_number = randint(1, 100), randint(1, 100)
    arithmetic_operation = arithmetic_operations[randint(0, 2)]
    expression = f'{first_number} {arithmetic_operation} {second_number}'
    print(f'Question: {expression}')

    if (arithmetic_operation == "+"):
        correct_answer = first_number + second_number
    elif (arithmetic_operation == "-"):
        correct_answer = first_number - second_number
    elif (arithmetic_operation == "*"):
        correct_answer = first_number * second_number

    answer = prompt.string('Your answer: ')
    return is_correct_answer(answer, str(correct_answer))
