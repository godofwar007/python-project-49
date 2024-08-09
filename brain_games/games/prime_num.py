#!/usr/bin/env python3

from random import randint
from colorama import Fore, init
init(autoreset=True)


rules = (f'Answer {Fore.GREEN}"yes"'
         f'{Fore.RESET} if given number is prime.'
         f' Otherwise answer'
         f'{Fore.RED} "no".')


def prime_number(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def correct_answer_question():
    number = randint(1, 1000)
    question = (f'Question: {number}')
    if prime_number(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
