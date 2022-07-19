from random import randint


GREET_MESSAGE = 'What is the result of the expression?'


def stage():
    arithmetic_operations = ['+', '-', '*']
    first_number, second_number = randint(1, 100), randint(1, 100)
    arithmetic_operation = arithmetic_operations[randint(0, 2)]
    question = f'{first_number} {arithmetic_operation} {second_number}'

    if (arithmetic_operation == "+"):
        correct_answer = first_number + second_number
    elif (arithmetic_operation == "-"):
        correct_answer = first_number - second_number
    elif (arithmetic_operation == "*"):
        correct_answer = first_number * second_number

    return [question, str(correct_answer)]
