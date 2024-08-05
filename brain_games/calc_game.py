#!/usr/bin/env python3

import prompt
from random import randint, choice
from colorama import Fore, init
init(autoreset=True)


def welcome_user_calc_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('What is the result of the expression?')
    print(f'{Fore.GREEN}*if the result is negative, '
          f'enter ure answer without "-".')
    return name


def random_question():
    first_num = randint(1, 100)
    second_num = randint(1, 100)
    expressions = ['+', '-', '*']
    expression = choice(expressions)

    if expression == '+':
        correct_answer = first_num + second_num
    elif expression == '-':
        if first_num >= second_num:
            correct_answer = first_num - second_num
            question = f'{first_num} - {second_num}'
        else:
            correct_answer = second_num - first_num
            question = f'{second_num} - {first_num}'
    elif expression == '*':
        correct_answer = first_num * second_num
    question = f'{first_num} {expression} {second_num}'
    return question, correct_answer


def correct_expression():
    name = welcome_user_calc_game()
    correct_answers = 0

    while correct_answers < 3:
        question, correct_answer = random_question()
        print(f'Question: {question}')
        user_answer = prompt.integer('Your answer is: ')
        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f'"{user_answer}" is wrong answer ;(. Correct answer '
                  f'was "{correct_answer}".')
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
