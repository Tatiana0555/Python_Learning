# Домашняя работа по теме: "Циклы"
# Формулировка задания: Реализовать скрипт, вычисляющий разность квадрата суммы и суммы квадратов.

# математическая формула: (a + b) ** 2 - (a ** 2 + b ** 2)

print('Данная программа позволит вычислить разность квадрата суммы и суммы квадратов двух чисел а и b.')
print('Математическая формула: (a + b) ** 2 - (a ** 2 + b ** 2)')

while True:
    a = int(input('Введите число a: \n'))
    b = int(input('Введите число b: \n'))
    c = ((a + b) ** 2) - (a ** 2 + b ** 2)
    print(f'Результат вычисления: {c}')
    choice = input('Хотите продолжить вычисления?(Да/нет) ').lower()
    if choice == 'нет':
        break