#!/usr/bin/env python3

from random import randint
from colorama import Fore, init
init(autoreset=True)


rules = (f'Answer {Fore.GREEN}"yes"'
         f'{Fore.RESET} if the number is even,'
         f' otherwise answer'
         f'{Fore.RED} "no".')


def is_even(number):
    return number % 2 == 0


def correct_answer_question():
    number = randint(1, 100)
    question = (f'Question: {number}')
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
