#!/usr/bin/env python3

import prompt
from random import randint
from brain_games.cli import name


def welcome_user_progression():
    print(f'Hello, {name}')
    print('What number is missing in the progression?')
    return 


def my_progression():
    start = randint(1, 50)
    step = randint(2, 10)
    length = randint(5, 10)
    progression = [start + i * step for i in range(length)]
    return progression


def replace_el():
    progression = my_progression()
    element = randint(0, len(progression) - 1)
    old_el = progression[element]
    progression[element] = '..'
    return progression, old_el


def progress_game():
    name = welcome_user_progression()
    correct_answers = 0

    while correct_answers < 3:
        progression, old_el = replace_el()
        correct_answer = old_el
        print('Question:', ' '.join(map(str, progression)))
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
