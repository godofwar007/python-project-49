#!/usr/bin/env python3

import prompt
from random import randint
from colorama import Fore, init
init(autoreset=True)
from brain_games.cli import name


def welcome_user_prime_game():
    print(f'Hello, {name}')
    print(f'Answer {Fore.GREEN}"yes"'
          f'{Fore.RESET} if given number is prime.'
          f' Otherwise answer'
          f'{Fore.RED} "no".')
    return 


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


def game_prime_n():
    name = welcome_user_prime_game()
    correct_answers = 0
    while correct_answers < 3:
        number = randint(1, 1000)
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')
        if prime_number(number):
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
