def engine(question, corr_answer, name):
    import prompt
    right_answers = 0
    while True:
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
        print(f"Let's try again, {name}!")
        break
    if right_answers == 3:
        print(f"Congratulations, {name}!")
