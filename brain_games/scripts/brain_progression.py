#!/usr/bin/env python

from brain_games.greet.greeting import welcome_user
from brain_games.games.progression import progression_stage
from brain_games.verification.game_cycle import guessing_cycle


def main():
    username = welcome_user()
    print('What number is missing in the progression?')
    guessing_cycle(username, progression_stage)


if __name__ == '__main__':
    main()
