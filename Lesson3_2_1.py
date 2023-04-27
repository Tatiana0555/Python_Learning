print('welcome'.istitle())
print('welcome'.title())
# преобразует слово, начинающееся со строчной, в слово с заглавной

# мы можем перебрать строку с помощью цикла, т.к. тип данных итерируемый
# range - метод, который возвращает последовательность от нуля (если не указываем другое) до какого-то другого числа
# мы говорим: пробегись по такому-то диапазону. В качестве диапазона мы должны указать кол-во (длину)  нашей строки

city = 'Moscow'
for i in range(len(city)):
      print(city[i], end=' ')
print()
print('hello')
#
for char in city:
      print(char)

list_number = [1, 2, 3, 4, 5, 6]
for number in list_number:
    if number % 2 == 0:
           print(number)













