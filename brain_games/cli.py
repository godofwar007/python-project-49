#!/usr/bin/env python3

import prompt
from .scripts.brain_calc import main as calc
from .scripts.brain_gcd import main as gcd
from .scripts.brain_even import main as even
from .scripts.brain_prime import main as prime
from .scripts.brain_progression import main as progression


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}, choose game, with input number of the game:')
    return name

def games():
    print('1. You need to calculate the result of the expression')
    print('2. You need to find the greatest common divisor of given numbers.')
    print('3. Answer "yes" if the number is even, otherwise answer "no".')
    print('4. Answer "yes" if given number is prime, otherwise answer "no".')
    print('5. You need to find missing number in the progression')
    game = prompt.integer('May I have your name? ')
    if game == 1:
        calc()
    elif game == 2:
        gcd()
    elif game == 3:
        even()
    elif game == 4:
        prime()
    elif game == 5:
        progression()       
    return 
