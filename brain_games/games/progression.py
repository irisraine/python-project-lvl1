from random import randint
from brain_games.common.engine import is_correct_answer
import prompt


GREET_MESSAGE = 'What number is missing in the progression?'


def stage():
    progression_length = randint(5, 10)
    progression_start = randint(1, 25)
    progression_step = randint(2, 7)
    progression_hidden_element_position = randint(0, progression_length - 1)
    progression = []
    progression_as_string = ""

    for i in range(progression_length):
        progression.append(progression_start + i * progression_step)
        if (i != progression_hidden_element_position):
            progression_as_string += f'{progression[i]} '
        else:
            progression_as_string += '.. '

    print(f'Question: {progression_as_string}')
    answer = prompt.string('Your answer: ')
    correct_answer = progression[progression_hidden_element_position]
    return is_correct_answer(answer, str(correct_answer))
