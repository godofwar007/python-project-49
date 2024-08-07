#!/usr/bin/env python3

import prompt
from random import randint
from colorama import Fore, init
init(autoreset=True)
from brain_games.cli import name


def welcome_user_brain_even():
    print(f'Hello, {name}')
    print(f'Answer {Fore.GREEN}"yes"'
          f'{Fore.RESET} if the number is even,'
          f' otherwise answer'
          f'{Fore.RED} "no".')
    return 


def even_number(number):  # if even == True, if not == False.
    return number % 2 == 0


def brain_even():
    name = welcome_user_brain_even()
    correct_answers = 0

    while correct_answers < 3:
        random_number = randint(1, 50)
        print(f'Question: {random_number}')
        user_answer = prompt.string('Your answer: ')
        if even_number(random_number):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f'"{user_answer}" is wrong answer ;(. Correct answer '
                  f'was "{correct_answer}".')
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
