from random import *

num = randint(1, 101)
print('Привет, давай сыграем в числовую угадайку')


def is_valid(user_num):
    for i in user_num:
        if i.isalpha():
            return False
    return float(user_num) == int(user_num)


guess = input('Введи число от 1 до 100')

while not is_valid(guess):
    guess = input('Надо ввести целое число')


print(num, guess)
