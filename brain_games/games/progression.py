from random import randint


GREET_MESSAGE = 'What number is missing in the progression?'


# Единичный этап игры
def single_game_stage():
    LENGTH_LOWER_LIMIT = 5
    LENGTH_UPPER_LIMIT = 10
    START_LOWER_LIMIT = 1
    START_UPPER_LIMIT = 25
    STEP_LOWER_LIMIT = 2
    STEP_UPPER_LIMIT = 7

    progression_length = randint(LENGTH_LOWER_LIMIT, LENGTH_UPPER_LIMIT)
    progression_start = randint(START_LOWER_LIMIT, START_UPPER_LIMIT)
    progression_step = randint(STEP_LOWER_LIMIT, STEP_UPPER_LIMIT)
    progression_hidden_element_position = randint(0, progression_length - 1)
    question = ""
    for i in range(progression_length):
        current_progression_element = progression_start + i * progression_step
        if i != progression_hidden_element_position:
            question += f'{current_progression_element} '
        else:
            question += '.. '
            correct_answer = current_progression_element
    return question, str(correct_answer)
