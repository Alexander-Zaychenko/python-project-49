from brain_games.cli import welcome_user
from random import randint, choice
from operator import add, sub, mul
import prompt


def check(answer, correct_answer):
    return answer == correct_answer


def print_question(question):
    print(f'Question: {question}')


def print_correct():
    print('Correct!')


def print_incorrect(answer, correct_answer, name):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
    print(f"Let's try again, {name}!")


def generate_question_even():
    num = randint(1, 100)
    even_or_odd_num = 'yes' if not num % 2 else 'no'
    return num, even_or_odd_num


def generate_question_calc():
    operators = {
        '+': add,
        '-': sub,
        '*': mul,
    }
    operand_left = randint(1, 50)
    operand_right = randint(1, 50)
    operator = choice(list(operators.keys()))
    question = f"{operand_left} {operator} {operand_right}"
    correct_answer = operators[operator](operand_left, operand_right)
    return question, str(correct_answer)


def generate_question_gcd():
    first = randint(1, 100)
    second = randint(1, 100)
    question = f'{first} {second}'
    if not first % second:
        answer = second
    elif not second % first:
        answer = first
    else:
        while first != 0 and second != 0:
            if first > second:
                first = first % second
            else:
                second = second % first
        answer = first + second
    return question, str(answer)


def generate_question_progression():
    step = randint(1, 4)
    progression = list(range(1, 50))[step::step]
    progression = progression[:10]
    question_index = randint(0, 9)
    answer = progression[question_index]
    progression[question_index] = '..'
    return ' '.join(map(str, progression)), str(answer)


def engine(game, rules):
    right_answers = 0
    wins_for_win = 3

    name = welcome_user()
    print(rules)
    while right_answers != 3:
        question, correct_answer = games[game]()
        print_question(question)
        answer = prompt.string('Your answer: ')
        if check(answer, correct_answer):
            print_correct()
            right_answers += 1
        else:
            print_incorrect(answer, correct_answer, name)
            break
        if right_answers == wins_for_win:
            print(f"Congratulations, {name}!")


games = {
    'brain-even': generate_question_even,
    'brain-calc': generate_question_calc,
    'brain-gcd': generate_question_gcd,
    'brain-progression': generate_question_progression,
}

