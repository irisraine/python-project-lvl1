from random import randint


GREET_MESSAGE = 'What number is missing in the progression?'


def stage():
    progression_length = randint(5, 10)
    progression_start = randint(1, 25)
    progression_step = randint(2, 7)
    progression_hidden_element_position = randint(0, progression_length - 1)
    progression = []
    question = ""

    for i in range(progression_length):
        progression.append(progression_start + i * progression_step)
        if (i != progression_hidden_element_position):
            question += f'{progression[i]} '
        else:
            question += '.. '

    correct_answer = progression[progression_hidden_element_position]
    return [question, str(correct_answer)]
