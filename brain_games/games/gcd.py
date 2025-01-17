from random import randint
from math import gcd


RULES = 'Find the greatest common divisor of given numbers.'


def get_correct_answer_question():
    first_num = randint(1, 100)
    second_num = randint(1, 100)
    correct_answer = gcd(first_num, second_num)
    question = (f'Question: {first_num} {second_num}')
    return question, correct_answer
