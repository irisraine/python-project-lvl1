#!/usr/bin/env python

from brain_games.greet.greeting import welcome_user
from brain_games.games.even import even_stage
from brain_games.verification.game_cycle import guessing_cycle


def main():
    username = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    guessing_cycle(username, even_stage)


if __name__ == '__main__':
    main()