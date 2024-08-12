from random import randint
from colorama import Fore, init
init(autoreset=True)


RULES = (f'Answer {Fore.GREEN}"yes"'
         f'{Fore.RESET} if the number is even,'
         f' otherwise answer'
         f'{Fore.RED} "no".')


def is_even(number):
    return number % 2 == 0


def get_correct_answer_question():
    number = randint(1, 100)
    question = (f'Question: {number}')
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer
