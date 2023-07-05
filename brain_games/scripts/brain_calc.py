from brain_games.cli import welcome_user
from ..engine import engine


def main():
    name = welcome_user()
    game = 'brain-calc'
    print('What is the result of the expression?')
    engine(game, name)

