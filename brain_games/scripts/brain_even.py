from brain_games.cli import welcome_user
from ..engine import engine


def main():
    name = welcome_user()
    game = 'brain-even'
    print('Answer "yes" if the number is even, otherwise answer "no".')
    engine(game, name)

