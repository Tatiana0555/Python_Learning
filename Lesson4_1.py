# number = 5
# if number % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')

# age = 32
# if age == 35:
#     print('Вам 35 лет')
# elif age < 35:
#     print('Вам меньше 35 лет')
# elif age > 35:
#     print('Вам больше 35 лет')
# elif age >= 35:
#     print('вам 35 лет или больше')
# elif age <= 35:
#     print('Вам 35 лет или меньше')
# elif age != 35:
#     print('Вам не 35 лет')

# if '5' == 5:
#     print('Равны')
# else:
#     print('Не равны')

# flag = True
# while flag:
#     print('1-Добавить\n2-изменить\n3-удалить')
#     choice = input('Введите число:  ')
#     if choice == "1":
#         print('Добавить')
#         flag = False
#     elif choice == '2':
#         print('Изменить')
#         flag = False
#     elif choice == '3':
#         print('Удалить')
#         flag = False
#     else:
#         print('Вы ошиблись. Такого пункта нет')
#         flag = True

# print('1-Добавить\n2-изменить\n3-удалить')
# choice = input('Введите число:  ')
# match choice:
#     case '1':
#         print('YES')
#     case '2':
#         print('YES')
#     case '3':
#         print('YES')
#     case _:
#         print('Вы ошиблись. Такого пункта нет')

# print('1-Добавить\n2-Изменить\n3-Удалить')
# choice = input('Введите число:  ')
# match choice:
#     case '1' | '2' | '3':
#         print('YES')
#     case _:
#         print('Вы ошиблись. Такого пункта нет')

# number = 3
# if number > 1 and number < 5:
#     print('YES')
# if 1 <  number < 5:
#     print('YES')

# money = False
# product = True
# if money is True and product is True:
#     print('Вы можете купить')
# else:
#     print('ERROR')

# money = False
# product = False
# if money is True or product is True:
#     print('YES')
# else:
#     print('NO')

season = ''
num = int(input('Введите номер месяца '))
match num:
    case 1 | 2 | 12:
        season = 'Зима'
    case 3 | 4 | 5:
        season = 'Весна'
    case 6 | 7 | 8:
        season = 'Лето'
    case 9 | 10 | 11:
        season = 'Осень'
    case _:
        print('Ошибка')
print(season)

# if num == 12 or 0 < num <= 2:
#     season = 'Зима'
# elif 3 <= num <= 5:
#     season = 'Весна'
# elif 6 <= num <= 8:
#     season = 'Лето'
# elif 9 <= num <= 11:
#     season = 'Осень'
# print(season)