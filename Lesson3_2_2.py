print('Угадай слово по буквам!')
secret_word = 'apple'
for _ in range(len(secret_word)):
     print('*', end= ' ')
print()
user_chars = []
attempts = 3
while attempts > 0:
    isWin = True
    user_char = input('Введите букву: ')
    user_chars.append(user_char)
    for char in secret_word:
         if char in user_chars:
            print(char, end=' ')
         else:
            print('*', end=' ')
            isWin = False
    print()
    if user_char not in secret_word:
        attempts -=1
    if attempts == 0:
        print('Вы проиграли')
        print(f'Секретное слово {secret_word}')
    if isWin is True:
        print('Вы победили!')
        break



