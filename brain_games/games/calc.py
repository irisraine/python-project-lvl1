from random import randint
from brain_games.verification.is_correct import is_correct_answer
import prompt


def calc_stage():
    arithmetic_operations = ['+', '-', '*']
    current_first_quiz_number, current_second_quiz_number = randint(1, 100), randint(1, 100)
    current_arithmetic_operation = arithmetic_operations[randint(0, 2)]
    current_expression = f'{current_first_quiz_number} {current_arithmetic_operation} {current_second_quiz_number}'
    print(f'Question: {current_expression}')
    current_correct_answer = eval(current_expression)
    current_answer = prompt.string('Your answer: ')
    if (is_correct_answer(current_answer, str(current_correct_answer))):
        return True
