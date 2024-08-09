#!/usr/bin/env python3

from random import randint


rules = 'What number is missing in the progression?'

def my_progression():
    start = randint(1, 50)
    step = randint(2, 10)
    length = randint(5, 10)
    progression = [start + i * step for i in range(length)]
    return progression


def correct_answer_question():
    progression = my_progression()
    element = randint(0, len(progression) - 1)
    old_el = progression[element]
    progression[element] = '..'
    hidden_el = ' '.join(map(str, progression))
    correct_answer = old_el
    question = (f'Question: {hidden_el}')
    return question, correct_answer
