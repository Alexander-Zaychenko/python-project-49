import prompt


def welcome_user():
    """Command Line Interface"""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name
