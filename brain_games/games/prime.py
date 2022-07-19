from random import randint


GREET_MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def stage():
    number = randint(1, 100)
    question = number
    correct_answer = "yes" if (is_prime(question)) else "no"
    return [question, correct_answer]


def is_prime(number):
    for i in range(2, number):
        if (number % i == 0):
            return False
    return True
