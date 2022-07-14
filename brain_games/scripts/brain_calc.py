#!/usr/bin/env python

from brain_games.greet.greeting import welcome_user
from brain_games.games.calc import calc_stage
from brain_games.verification.game_cycle import guessing_cycle


def main():
    username = welcome_user()
    print('What is the result of the expression?')
    guessing_cycle(username, calc_stage)


if __name__ == '__main__':
    main()
