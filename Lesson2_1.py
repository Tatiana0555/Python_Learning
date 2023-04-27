import random
secret_number = random.randint(1, 10)
print('Угадай число от 1 до 10.')
attempts = 3
while attempts > 0:
    user_number = int(input('Введите число от 1 до 10: '))
    if user_number == secret_number:
        print('Вы выиграли!')
        break
    elif user_number > secret_number:
        print('Секретное число меньше.')
    elif user_number < secret_number:
        print('Секретное число больше.')
    attempts -= 1
    if attempts == 0:
        print(f'Вы проиграли. Секретное число было {secret_number}.')
