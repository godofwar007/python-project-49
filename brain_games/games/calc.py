from random import randint, choice

RULES = 'What is the result of the expression?'


def get_correct_answer_question():
    first_num = randint(1, 100)
    second_num = randint(1, 100)
    expressions = ['+', '-', '*']
    expression = choice(expressions)
    question = (f'Question: {first_num} {expression} {second_num}')

    if expression == '+':
        correct_answer = first_num + second_num
    elif expression == '-':
        correct_answer = first_num - second_num
    elif expression == '*':
        correct_answer = first_num * second_num
    return question, correct_answer
