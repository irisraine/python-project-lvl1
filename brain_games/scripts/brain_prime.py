from brain_games.greet.greeting import welcome_user
from brain_games.games.prime import prime_stage
from brain_games.verification.game_cycle import guessing_cycle


def main():
    username = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    guessing_cycle(username, prime_stage)


if __name__ == '__main__':
    main()
