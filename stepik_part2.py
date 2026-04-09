# print('Подсчёт количества')
# counter = 0                                             # создаём переменную счётчика
# for _ in range(10):
#     num = int(input())
#     if num > 10:                                        # при выполнении условия 
#         counter = counter + 1                           # увеличиваем значение cчётчика

# print('Было введено', counter, 'чисел, больших 10.')
# counter1 = 0
# counter2 = 0
# for _ in range(10):
#     num = int(input())
#     if num > 10:
#         counter1 = counter1 + 1
#     if num == 0:
#         counter2 = counter2 + 1
# print('Было введено', counter1, 'чисел, больших 10.')
# print('Было введено', counter2, 'нулей.' )

# counter = 0
# for i in range(1, 101):
#     if i**2 % 10 == 4:
#         counter = counter + 1
# print(counter)

# print('Вычисление суммы и произведения')
# total = 0
# for _ in range(10):
#     num = int(input())
#     if num > 10:
#         total = total + num
# print('Сумма чисел больших 10 равна',  total)

# total = 0
# for i in range(1, 101):
#     total = total + i
# print('Сумма равна', total)

# print('Рассмотрим еще один пример: напишем программу, которая запрашивает 10 ' \
# 'целых чисел и находит их среднее значение:')
# total = 0
# for _ in range(10):
#     num = int(input())
#     total = total + num
# average = total / 10
# print('Среднее значение равно', average)

# print('Максимум и минимум')
# largest = 0
# for _ in range(10):
#     num = int(input())    
#     if num > largest:
#         largest = num
# print('Наибольшее число равно', largest) 

# largest = int(input())  # принимаем первое число за максимальное
# for _ in range(9):
#     num = int(input())
#     if num > largest:
#         largest = num
# print('Наибольшее число равно', largest) 

# counter = 0
# for i in range(1, 11):
#     if i % 2 == 1:
#         counter = counter + 1
# print(counter)  # 5

# counter = 0
# for i in range(20, 26):
#     if i >= 10:
#         counter = counter + 1
# print(counter)  # 6

# prod = 1
# for i in range(-7, -3, 1):
#     if i < -5:
#         prod = prod * i
# print(prod)  # 42

# total = 0
# counter = 0
# even = 0
# greater_than_6 = 0

# for i in range(10, 4, -1):
#     total = total + i
#     counter = counter + 1
#     last = i

#     if i % 2 == 0:
#         even = even + 1
#     if i > 6:
#         greater_than_6 = greater_than_6 + 1
# print(total)
# print(counter)
# print(even)
# print(greater_than_6)

# total_len = 0
# for _ in range(3):
#     word = input()
#     total_len = total_len + len(word)
# print(total_len)

# print('Сигнальные метки, Напишем программу, ' \
# 'определяющую, что натуральное число является простым:')
# num = int(input())
# flag = True
# for i in range(2, num):
#     if num % i == 0:  #  если исходное число делится на какое-либо отличное от 1 и самого себя
#         flag = False
# if num == 1:
#     print('Это единица, она не простая и не составная') 
# elif flag == True:
#     print('Число простое')
# else:
#     print('Число составное')

# total = 0
# for i in range(1, 10):
#     if i % 2 == 1:
#         total += i
# print(total)  # 25

# total1 = 0
# total2 = 0
# for _ in range(5):
#     num = int(input())
#     if 2 <= num < 5:
#         total1 += num
#     if abs(num) <= 3:
#         total2 += num
# print(total1, total2)

# total = 0
# for i in range(1, 6):
#     total += i
# print(total)  # 15

# total = 0
# for i in range(1, 6):
#     total += i
#     print(total, end='')  # 1361015

# print('Количество чисел')
# print('На вход программе подаются два целых числа a и b (a ≤ b). ' \
# 'Напишите программу, которая подсчитывает количество чисел в диапазоне ' \
# 'от a до b (включительно), куб которых оканчивается на 4 или 9.')

# a, b = int(input()), int(input())
# count = 0
# for i in range(a, b + 1):
#     if (i ** 3) % 10 == 4 or (i ** 3) % 10 == 9:
#         count +=1
# print(count)

# print('Сумма чисел')
# print('На вход программе подаются натуральное число n, а затем n целых чисел, ' \
# 'каждое на отдельной строке. Напишите программу, которая подсчитывает сумму ' \
# 'введённых чисел (не включая само число n). ')
# count = 0
# n = int(input())
# for i in range(n):
#     m = int(input())
#     count += m
# print(count)

# print('Асимптотическое приближение')
# print('''1. Не забывайте про импорт модуля math, логарифм без него не будет работать.' \
# '2. Создайте переменную, у меня это num = 0.' \
# '3. range начинайте с цифры 1 до n , чтобы не начиналось с нуля.' \
# '4. num равно num + (1 / ( i  +  1), где первая единица - числитель, а ' i  + 1 ' знаменатель.'
# 'Тоесть сейчас мы решили дробные уравнения 1/2 + 1/3 + 1/4 ..... 1 / n. '
# 'Первую единицу и логарифм мы не считали.'
# '5. Вводим num2. num 2 = num + 1 ( та единица которую упустили) + логарифм.6. print (num2)''')
# import math
# num = 0
# n = int(input())
# for i in range(1, n + 1):
#     num += 1 / i
#     num2 = num - math.log(n)
# print(num2)

# print('Сумма чисел 2')
# print('На вход программе подаётся натуральное число n. ' \
# 'Напишите программу, которая подсчитывает сумму тех чисел от 1 до n (включительно), ' \
# 'квадрат которых оканчивается на 2, на 5 или на 8.')
# total = 0
# n = int(input())
# for i in range(1, n + 1):
#     if (i ** 2) % 10 == 2 or (i ** 2) % 10 == 5 or (i ** 2) % 10 == 8:
#         total += i
# print(total)

# print('Факториал ❗')
# x = int(input())
# count = 1
# for i in range(1, x + 1):
#     count *= i
# print(count)

# print('Без нулей 0️')
# print('Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.')
# y = 1
# for i in range(10):
#     x = int(input())
#     if x != 0:
#         y *= x
# print(y)

# print('Сумма делителей')
# y = 0
# x = int(input())
# for i in range (1, x+1):
#     if x % i == 0:
#         y += i
# print(y)