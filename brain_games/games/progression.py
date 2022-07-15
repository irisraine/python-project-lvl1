from random import randint
from brain_games.common.engine import is_correct_answer
import prompt


GREET_MESSAGE = 'What number is missing in the progression?'


def stage():
    progression_length = randint(5, 10)
    progression_start = randint(1, 25)
    progression_step = randint(2, 7)
    progression_hidden_element_position = randint(0, progression_length - 1)
    current_progression = []
    current_progression_as_string = ""

    for i in range(progression_length):
        current_progression.append(progression_start + i * progression_step)
        if (i != progression_hidden_element_position):
            current_progression_as_string += f'{current_progression[i]} '
        else:
            current_progression_as_string += '.. '

    print(f'Question: {current_progression_as_string}')
    current_answer = prompt.string('Your answer: ')
    current_correct_answer = current_progression[progression_hidden_element_position]
    return is_correct_answer(current_answer, str(current_correct_answer))
