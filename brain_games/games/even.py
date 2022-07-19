from random import randint


GREET_MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'


def stage():
    number = randint(1, 100)
    question = number
    correct_answer = "yes" if (question % 2 == 0) else "no"
    return [question, correct_answer]
