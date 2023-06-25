from brain_games.cli import welcome_user
from random import randint
import prompt


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    right_answers = 0

    while right_answers < 3:
        question = randint(1, 100)

        corr_answer = 'yes'
        if question % 2:
            corr_answer = 'no'

        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if (not question % 2 and answer == corr_answer) or\
                (question % 2 and answer == corr_answer):
            print('Correct!')
            right_answers += 1
            continue
        print(
            f"'{answer}' is wrong answer ;(. Correct answer was '{corr_answer}'"
        )
        right_answers = 0

    print(f"Congratulations, {name}!")
