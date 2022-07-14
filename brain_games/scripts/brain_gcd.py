#!/usr/bin/env python

from brain_games.greet.greeting import welcome_user
from brain_games.games.gcd import gcd_stage
from brain_games.verification.game_cycle import guessing_cycle


def main():
    username = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    guessing_cycle(username, gcd_stage)


if __name__ == '__main__':
    main()
