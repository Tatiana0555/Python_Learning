secret_number = 5
print('Угадай число от 1 до 10.')
attempts = 3
while attempts > 0:
    user_number = int(input('Введите число от 1 до 10: '))
    if user_number == secret_number:
        print('Вы угадали!')
        break
    elif user_number < secret_number:
        print('Секретное число больше.')
    elif user_number > secret_number:
        print('Секретное число меньше.')
    attempts -= 1
    if attempts == 0:
        # print('Вы проиграли!' + str(secret_number)) - конкатенация
        print(f'Вы проиграли! Секретное число было {secret_number}.')

