#!/usr/bin/env python3

import prompt
from random import randint, choice

rules = 'What is the result of the expression?'

def correct_answer_question():
    first_num = randint(1, 100)
    second_num = randint(1, 100)
    expressions = ['+', '-', '*']
    expression = choice(expressions)

    if expression == '+':
        correct_answer = first_num + second_num
    elif expression == '-':
        correct_answer = max(first_num, second_num) - min(first_num, second_num)
    elif expression == '*':
        correct_answer = first_num * second_num
    question = f'{first_num} {expression} {second_num}'
    return question, correct_answer
