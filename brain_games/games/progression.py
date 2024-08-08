#!/usr/bin/env python3

import prompt
from random import randint


rules = 'What number is missing in the progression?'

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


def correct_answer_question():
    progression, old_el = replace_el()
    correct_answer = old_el
    question = ('Question:', ' '.join(map(str, progression)))
    return correct_answer, question
