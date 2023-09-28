from random import *

num = randint(1, 100)
print('Привет, давай сыграем в числовую угадайку')


def is_valid(user_num):
    for i in user_num:
        if i.isalpha():
            return False

    n = float(user_num)
    if not 0 < n < 101:
        return False

    return n == int(n)


guess = input('Введите число от 1 до 100')

while True:
    while not is_valid(guess):
        guess = input('Надо ввести целое число от 1 до 100')
    n = int(guess)

    if n == num:
        break
    elif n < num:
        guess = input('Твое число меньше загаданного, попробуйте еще разок')
        continue
    else:
        guess = input('Твое число больше загаданного, попробуйте еще разок')

print('Поздравляю, ты угадал!')
print('Спасибо за игру , еще уидимся...)')
