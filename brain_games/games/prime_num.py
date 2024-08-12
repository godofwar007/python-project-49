from random import randint
from colorama import Fore, init
init(autoreset=True)


RULES = (f'Answer {Fore.GREEN}"yes"'
         f'{Fore.RESET} if given number is prime.'
         f' Otherwise answer'
         f'{Fore.RED} "no".')


def is_prime_number(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_correct_answer_question():
    number = randint(1, 1000)
    question = (f'Question: {number}')
    correct_answer = 'yes' if is_prime_number(number) else 'no'
    return question, correct_answer
