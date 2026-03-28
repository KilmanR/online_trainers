# sep1 = '#'
# end2 = '?'
# print('YES', 'NO', sep=sep1, end='+')
# print('MAYBE', 'NEVER', sep='*', end=end2)
# print('I', 'like', 'Python', sep='***')

# name = input()
# print('Привет,', name, end='!')

# sep = input()
# str_1 = input()
# str_2 = input()
# str_3 = input()
# print(str_1, str_2, str_3, sep=sep)

# x = 3
# y = 4
# z = x + y
# z = z + 1 
# x = y
# y = 5
# x = z + y + 7
# print(x)

# a = int(input())
# b = a + 1
# c = b + 1
# print(a, b, c, sep = '\n')

# a = int(input())
# b = int(input())
# c = int(input())
# d = a + b + c
# print(d)

# monitor = int(input())
# pc = int(input())
# kb = int(input())
# mouse = int(input())
# full_pc = monitor + pc + kb + mouse
# print(full_pc * 3)

# a = int(input())
# b = int(input())
# c = 3 * (a + b) **3 + 275 * b ** 2 - 127 * a - 41
# print(c)

# a = int(input())
# print('Следующее за числом', a, 'число:', a + 1)
# print('Для числа', a, 'предыдущее число:', a - 1)

# z = int(input())
# v = z ** 3
# s = 6 * z ** 2
# print('Обьём =', v)
# print('Площадь полной поверхности =', s)

# a1 = int(input())
# d = int(input())
# n = int(input())
# an = a1 + d * (n - 1)
# print(an)

# print((-10)**2)
# print((-10)**3)
# print(3**1**2)
# print(23 % 7)
# print(20 % 5)
# print(2 % 5)
# print(123 % 10)
# print(23 // 7)
# print(20 // 5)
# print(2 // 5)
# print(123 // 10)
# print(-123 // 10)

# a = 15 // (16 % 7)
# b = 34 % a * 5 - 29 % 5 * 2
# print(a + b)
# a = 82 // 3**2 % 7
# print(a)

# b1 = int(input())
# q = int(input())
# n = int(input())
# bn = b1 * q ** (n - 1)
# print(bn)

# sh = int(input())
# m = int(input())
# print(m // sh)
# print(m % sh)

# z = int(input())
# y = z // 2
# x = z % 2
# print(y + x)

# x = int(input())
# y = x // 60
# z = x % 60
# print(x, 'мин - это', y, 'час', z, 'минут.')

# x = int(input())
# d1 = x % 10
# d2 = (x % 100) // 10
# d3 = x // 100
# # print(d1 + d2 + d3)
# # print( d1 * d2 * d3)
# print(d1, d2, d3, sep="")
# print(d2, d3, d1)

# print('*' * 17)
# print('*', ' ' * 14, end='*')
# print()
# print('*', ' ' * 14, end='*')
# print()
# print('*' * 17)

# num_1 = int(input())
# num_2 = int(input())

# q_sum = (num_1 + num_2) ** 2
# sum_q = (num_1 ** 2) + (num_2 ** 2)

# print('Квадрат суммы', num_1, 'и', num_2, 'равен', q_sum)
# print('Сумма квадратов', num_1, 'и', num_2, 'равна', sum_q) 

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# print((a ** b) + (c**d)) 

# n = int(input())
# result = n * 123
# print(result)

# a = int(input())
# b = int(input())
# c = int(input())
# z = a + a
# x = a + b
# if z == b and x == c:
#     print('YES')
# else:
#     print('NO') 

# level = 5
# has_training = True
# level_message ='None'

# if level >= 1 and level <= 5:
#     message = 'Basic weapons only'
# elif level >= 6 and level <= 10:
#     if has_training:
#         message = 'Access to advanced weapons granted'
#     elif not has_training:
#         message = 'Need weapon training first'
# elif level > 10:
#     message = 'Access to all weapons granted'
# else:
#     message = 'Invalid level'
# print(level_message)      

# num = int(input())  
# d1 = (num // 10 ** 3) % 10
# d2 = (num // 10 ** 2) % 10
# d3 = (num // 10 ** 1) % 10
# d4 = (num // 10 ** 0) % 10
# if d1 + d4 == d2 - d3:
#     print('YES')
# else:
#     print('NO')

# a = int(input())
# b = int(input())
# c = int(input())

# if a > 0 and b > 0 and c > 0:
#     print(a + b + c)
# elif a > 0 and b > 0:
#     print(a + b)
# elif a > 0 and c > 0:
#     print(a + c)
# elif b > 0 and c > 0:
#     print(b + c)
# else:
#     print('0')

# age = int(input())
# if age > 0 and age <= 13:
#     print('детство')
# elif age >= 14 and age <= 24:
#     print('молодость')
# elif age >= 25 and age <= 59:
#     print('зрелость')
# elif age >= 60:
#     print('старость')

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# if a < b:
#     ab = a
# else:
#     ab = b
# if c < d:
#     cd = c
# else:
#     cd = d
# if ab < cd:
#     abcd = ab
# else:
#     abcd = cd
# print(abcd)

# num = int(input())
# d1 = (num // 10 ** 2) % 10
# d2 = (num // 10 ** 1) % 10
# d3 = (num // 10 ** 0) % 10
# print(d1, d2, d3, sep='--')

# x = int(input())
# if (-30 < x <= -2) or (7 < x <= 25):
#     print('Принадлежит')
# else:
#     print('Не принадлежит')

# num = int(input())
# if num % 7 == 0 or num % 17 == 0:
#     print('YES')
# else:
#     print('NO')

# a, b, c = int(input()), int(input()), int(input())
# if a < 0 or b < 0 or c < 0:
#     print('Error')
# elif a + b > c and a + c > b and b + c > a:
#     print('YES')
# else:
#     print('NO')
# a, b, c, d = int(input()), int(input()), int(input()), int(input())

# if (a == c and b != d) or (a != c and b == d):
#     print('YES')
# else:
#     print('NO') 

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if ((a + 1 == c or a - 1 == c) and b == d) or ((b + 1 == d or b - 1 == d) and a == c) or ((a + 1 == c or a -1 == c) and (b + 1 == d or b - 1 == d)):
#     print('YES')
# else:
#     print('NO')  

# a, b, c = int(input()), int(input()), int(input())
# if a >= b >= c or c >= b >= a:
#     print(b)   
# elif b >= c >= a or a >= c >= b:
#     print(c)
# elif c >= a >= b or b >= a >= c:
#     print(a)

# month = int(input())

# if month == 2:
#     days = 28
# elif month == 4 or month == 6 or month == 9 or month == 11:
#     days = 30
# else:
#     days = 31

# print(days)

# m = int(input())
# if 0 < m < 60:
#     print('Легкий вес')
# elif 60 <= m < 64:
#     print('Первый полусредний вес')
# elif 64 <= m < 69:
#     print('Полусредний вес')

# a = int(input())
# b = int(input())
# op = input()
# if op == '+':
#     print(a + b)
# elif op == '-':
#     print(a - b)
# elif op == '*':
#     print(a * b)
# elif op == '/':
#     if b == 0:
#         print('На ноль делить нельзя!')
#     elif b != 0:
#         print(a / b)
# else:
#     print('Неверная операция')

# a = input()
# b = input()

# if (a == 'красный' or a == 'синий' or a == 'желтый') and (b == 'красный' or b == 'синий' or b == 'желтый'):
#     if  a == b:
#         print(a)
#     elif (a == 'красный' and b == 'синий') or (b == 'красный' and a == 'синий'):
#         print('фиолетовый')
#     elif (a == 'синий' and b == 'желтый') or (b == 'синий' and a == 'желтый'):
#         print('зеленый')
#     elif (a == 'красный' and b == 'желтый') or (b == 'красный' and a == 'желтый'):    
#         print('оранжевый')

# else:
#     print('ошибка цвета')

# a = int(input())

# if a == 0:
#     print('зеленый')
# elif 1 <= a <= 10:
#     if a % 2 == 0:
#         print('черный')
#     else:
#         print('красный')
# elif 11 <= a <= 18:
#     if a % 2 == 0:
#         print('красный')
#     else:
#         print('черный')
# elif 19 <= a <= 28:
#     if a % 2 == 0:
#         print('черный')
#     else:
#         print('красный')
# elif 29 <= a <= 36:
#     if a % 2 == 0:
#         print('красный')
#     else:
#         print('черный')
# else:
#     print('ошибка ввода')

# a1 = int(input())
# b1 = int(input())
# a2 = int(input())
# b2 = int(input())
# if (a1 < a2) and (b1 < a2) or (a2 < a1) and (b2 < a1):
#     print('пустое множество')
# elif (a1 >= a2) and (b2 >= b1 >= a2):
#     if a1 == b1:
#         print(a1)
#     else:
#         print(a1, b1)
# elif (a2 >= a1) and (b1 >= b2 >= a1):
#     if a2 == b2:
#         print(a2)
#     else:
#         print(a2, b2)
# elif (a1 <= a2) and (a2 <= b1 <= b2):
#     if a2 == b1:
#         print(a2)
#     else:
#         print(a2, b1)
# elif (a2 <= a1) and (a1 <= b2 <= b1):
#     if a1 == b2:
#         print(a1)
#     else:
#         print(a1, b2)