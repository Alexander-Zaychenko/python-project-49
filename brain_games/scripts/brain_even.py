from ..engine import engine


def main():
    """run brain-even"""
    game = 'brain-even'
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    engine(game, rules)
