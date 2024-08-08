#!/usr/bin/env python3

import prompt
from random import randint
from math import gcd


def welcome_user_calc_gcd():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Find the greatest common divisor of given numbers.')
    return name


def solution_gcd():
    first_num = randint(1, 100)
    second_num = randint(1, 100)
    question = f'{first_num} {second_num}'
    correct_answer = gcd(first_num, second_num)
    return question, correct_answer


def result_gcd():
    name = welcome_user_calc_gcd()
    correct_answers = 0

    while correct_answers < 3:
        question, correct_answer = solution_gcd()
        print(f'Question: {question}')
        user_answer = prompt.integer('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f'"{user_answer}" is wrong answer ;(. Correct answer '
                  f'was "{correct_answer}".')
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
