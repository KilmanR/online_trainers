# print('Тема урока: цикл while')

# print('Цикл for VS цикл while')
# # используем for
# for i in range(101):
#     print(i)

# # используем while
# i = 0
# while i < 101:
#     print(i)
#     i += 1

# используем for
# for i in range(0, 100, 3):
#     print(i)

# # используем while
# i = 0
# while i < 100:
#     print(i)
#     i += 3

# i = 5
# while i <= 11:
#     print('Python awesome!')
#     i += 1

# i = 7
# a = 5
# while i < 11:
#     a += i
#     i += 2
# print(a)

# total = 1
# while total < 10:
#     num = int(input())
#     total *= num
#     print(total)


# words = []
# while True:
#     word = input()
#     if word == 'стоп' or word == 'хватит' or word == 'достаточно':
#         break
#     words.append(word)

# # for word in words:
# #     print(word)
# print(len(words))

# nums = []
# while True:
#     num = int(input())
#     if num % 7 != 0:
#         break
#     nums.append(num)
# for num in nums:
#     print(num)

# n = int(input())
# while n % 7 == 0:
#     print(n)
#     n = int(input())

# nums = []
# while True:
#     num = int(input())
#     if num < 0:
#         break
#     nums.append(num)
# print(sum(nums))

# print('Количество пятёрок 5️⃣')
# print('На вход программе подаётся последовательность целых чисел от 1 до 5, ' \
# 'характеризующее оценку ученика, каждое число на отдельной строке. ' \
# 'Концом последовательности является любое неположительное число либо число, большее 5. ' \
# 'Напишите программу, которая выводит количество пятерок.')
# count_fives = 0
# while True:
#     num = int(input())
    #     # Проверяем условие окончания последовательности: неположительное число или больше 5
#     if num <= 0 or num > 5:
#         break
    #     # Если число — пятёрка, увеличиваем счётчик
#     if num == 5:
#         count_fives += 1
# print(count_fives)

# print('Первый никнейм 👉')
# while True:
#     nick = input()
#     if '_' not in nick:
#         print(nick)
#         break

# print('Сколько ждать? ⏱️')
# count = 0
# found_alexandra = False
# while True:
#     name = input().strip()    
#     if name == "Александра":
#         found_alexandra = True
#         count = 0  # сбрасываем счётчик — начинаем отсчёт после Александры
#     elif name == "Левон":
#         if found_alexandra:
#                 # Нашли Левона после Александры — выводим результат и завершаем программу
#             print(count)
#             break
#     else:
#             # Обычное имя — если уже нашли Александру, увеличиваем счётчик
#         if found_alexandra:
#             count += 1


# print('Ведьмаку заплатите чеканной монетой')
# print('Всем известно, что ведьмак способен одолеть любых чудовищ, однако его услуги обойдутся недешево. К тому же ведьмак не принимает купюры, он принимает только чеканные монеты. В мире ведьмака существуют монеты с номиналами 1,5,10,25.Напишите программу, которая определяет, какое минимальное количество чеканных монет нужно заплатить ведьмаку.')
    
# total = int(input())
# count = 0
# while total > 0:
#     if total >= 25:
#         total -= 25
#         count += 1
#     elif total >= 10:
#         total -= 10
#         count += 1
#     elif total >= 5:
#         total -= 5
#         count += 1
#     else:
#         total -= 1
#         count += 1
# print(count)

# print('Временной промежуток')
# h1, m1, h2, m2 = int(input()), int(input()), int(input()), int(input())
# start = (h1 * 60) + m1
# end = (h2 * 60) + m2
# while start <= end:
#     h = start // 60
#     m = start % 60
#     print(f'{h:02d}:{m:02d}')
#     start += 1

# num = 1576
# has_seven = False                                 # сигнальная метка (флаг)
# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         has_seven = True
#     num = num // 10
# if has_seven == True:
#     print('YES')
# else:
#     print('NO')

# num = 8619
# n = len(str(num))
# for i in range(1, n + 1):
#     digit = num // 10 ** (n - i) % 10
#     print(i, '-я', ' цифра равна ', digit, sep='')
# 1-я цифра равна 8
# 2-я цифра равна 6
# 3-я цифра равна 1
# 4-я цифра равна 9

# num = 813
# while num > 0:
#     last_digit = num % 10
#     num //= 10
#     print(last_digit, sep='=', end='')
# num = 1265
# while num > 0:
#     last_digit = num % 10
#     if last_digit % 2 == 0:
#         print(last_digit)
#     num //= 10
# num = 1765
# while num > 0:
#     last_digit = num % 10
#     if 5 <= last_digit <= 9:
#         print('+', end='')
#     num //= 10
# num = 12345
# product = 1
# while num != 0:
#     last_digit = num % 10
#     product = product * last_digit
#     num = num // 10
# print(product)
# num = 725
# while num != 0:
#     last_digit = num % 10
#     num //= 10
#     print(last_digit, sep='', end='$')
# num = 586
# while num > 0:
#     last_digit = num % 10
#     print(last_digit, sep='*', end='#')
#     num //= 10
#     print()

# print('Обратный порядок 1')
# num = int(input())
# while num > 0:
#     l_d = num % 10
#     print(l_d)
#     num //= 10

# print('max и min')
# num = int(input())
# num_list = []
# while num > 0:
#     last_digit = num % 10
#     num_list.append(last_digit)
#     num //= 10
# num_list.sort()
# print(f'Максимальная цифра равна {num_list[-1]}\nМинимальная цифра равна {num_list[0]}')

# print('Все вместе')
# num = int(input())
# num_list = []
# while num > 0:
#     last_digit = num % 10
#     num_list.append(last_digit)
#     num //= 10
# sum_num_list = sum(num_list)
# prod = 1
# for num in num_list:
#     prod *= num
# prod_num = prod
# len_num = len(num_list)
# arg_num = sum_num_list / len_num
# first_num = num_list[-1]
# sum_first_end_digit = num_list[0] + num_list[-1]
# print(sum_num_list)
# print(len_num)
# print(prod_num)
# print(arg_num)
# print(first_num)
# print(sum_first_end_digit)

# print('Вторая цифра')
# num = int(input())
# num_list = []
# while num > 0:
#     last_digit = num % 10
#     num_list.append(last_digit)
#     num //= 10
# print(num_list[-2])

# print('Одинаковые цифры')
# num = int(input())
# num_list = []
# while num > 0:
#     last_digit = num % 10
#     num_list.append(last_digit)
#     num //= 10
# num_list.sort()    
# if num_list[0] == num_list[-1]:
#     print('YES')
# else:
#     print('NO')

# for i in range(8):
#     for j in range(6):
#         print('*', end='')
#     print()
# for i in range(8):
#     for j in range(i + 1):
#         print('*', end='')
#     print()
# for i in range(2):
#     for j in range(3):
#         print('C' * i + '+' * j)
# for i in range(1, 2):
#     print(i * 'C')
#     for j in range(2, 4):
#         print(j * '♨️')
#     for k in range(3, 1, -1):
#         print(k * '🐳')

# print('#')
# for i in range(1, 3):
#     for j in range(1, 3):
#         print(i * '🐍' + j * '🐝')

#     print(i * '🦀')
# for i in range(2):
#     print(i, end='*')
#     for j in range(2):
#         print('/', end='+')
# for i in range(2):
#     for j in range(2):
#         print('*', end='#')

#     for k in range(3):
#         print('%', end='&')

#     print()
# for i in range(1, 4):
#     for j in range(3, 5):
#         print(i + j, end='')
# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10

# print(counter)
# print('Таблица-1')
# print('Упорядоченные цифры')
# num = int(input())
# num_list = []
# while num > 0:
#     last_digit = num % 10
#     num_list.append(last_digit)
#     num //= 10
# if num_list == sorted(num_list):
#     print('YES')
# else:
#     print('NO')

# print('Таблица-2')
# num = int(input())
# for i in range (1, num + 1):
#     print(i, i, i, i, i )

# print('Таблица-3')
# num = int(input())
# for i in range (1, num + 1):
#     print('')
#     for j in range (1, 10):
#         print(f'{i} + {j} = {i + j}')

# print('Численный треугольник 1')
# num = int(input())
# for i in range(1, num + 1):
#     for j in range(1, i + 1):
#         continue
#     print(j * str(i))

# print('Звёздный треугольник 🌟🌶️')
# num = int(input())
# for i in range (1, num//2 + 2):
#     print('*' * i)
# for j in range (num//2 , 0, -1):
#     print('*' * j)

# total = 0
# for x in range(1, 65):
#     for y in range(1, 60):
#         if 12 * x + 13 * y == 777:
#             total += 1
#             print('x =', x, 'y =', y)
# print('Общее количество натуральных решений =', total)

# print('считаем месяцы!')
# total = 0
# for n in range(1, 28):
#     for k in range(1, 30):
#         for m in range(1, 31):
#             if 28 * n + 30 * k + 31 * m == 365:
#                 total += 1
#                 print('n =', n, 'k =', k, 'm =', m)
# print('Общее количество натуральных решений =', total)

# print('Старинная задача 🐮')
# print('Сколько быков, коров и телят можно купить ровно на 100 рублей, если плата за быка – 10 рублей, за корову – 5 рублей, за телёнка – 0.5 рубля и надо купить 100 голов скота?')
# bull = 0
# cow = 0
# calf = 0
# total = 0
# for bull in range(100):
#     for cow in range(100):
#         for calf in range(100):
#             if bull*10 + cow*5 + calf*0.5 == 100:
#                 if bull + cow + calf == 100:                        
#                     print(bull, cow, calf)
#                     break

# print('Гипотеза Эйлера о сумме степеней 🌶️')
# a = 0
# b = 0
# c = 0
# d = 0
# e = 0
# for a in range(1, 151):
#     for b in range(a, 151):
#         for c in range(b, 151):
#             for d in range(c, 151): 
#                 for e in range(d, 151):               
#                     if a**5 + b**5 + c**5 + d**5 == e**5:                        
#                         print(a, b, c, d, e)                
#                         print(a+b+c+d+e)

print('Делители-1')
num = int(input())
for i in range(1, num + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count +=1
    print(i, count * '+')
print('Четные цифры 2️⃣🌶️')

