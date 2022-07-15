import importlib
from brain_games.common.engine import welcome_user, guessing_cycle


def launch(game):
    username = welcome_user()
    game = f'brain_games.games.{game}'
    current_game = importlib.import_module(game)
    print(current_game.GREET_MESSAGE)
    guessing_cycle(username, current_game.stage)
