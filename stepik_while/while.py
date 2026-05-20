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

# print('Четные цифры 2️⃣🌶️')
# num = int(input())
# n = len(str(num))
# count = 0
# for i in range(1, n + 1):
#     digit = num // 10 ** (n - i) % 10
#     if digit % 2 == 0:
#         count += 1
#         if count > 0:
#             print(count, '-я', ' четная цифра равна ', digit, sep='')
# if count == 0:
#     print('Четных цифр в числе нет')

# num = int(input())                                # считываем число
# while num != 0:                                   # проверяем, что цифры числа не закончились
#     last_digit = num % 10                         # получаем последнюю цифру числа
#     ...                                           # обрабатываем последнюю цифру числа
#     num = num // 10                               # удаляем последнюю цифру из числа

# num = int(input())                                # считываем число
# n = len(str(num))                                 # количество разрядов числа
# for i in range(1, n + 1):                         # проходим по всем разрядам числа от 1 до n
#     digit = num // 10 ** (n - i) % 10             # получаем i-ю цифру числа
#     ...                                           # обрабатываем i-ю цифру числа

# num = int(input())
# flag = True

# for i in range(2, num):
#     if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
#         flag = False
#         break               # останавливаем цикл если встретили делитель числа        

# if flag:  # эквивалентно if flag == True:
#     print('Число простое')
# else:
#     print('Число составное')

# result = 0
# for i in range(10):
#     num = int(input())
#     if num < 0:
#         break
#     result += num
# print(result)

# num = int(input())
# number = num
# flag = False
# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         flag = True
#         break        # прерываем цикл, так как число гарантированно содержит цифру 7
#     num //= 10

# if flag:  # эквивалентно if flag == True:
#     print('Число', number, 'содержит цифру 7')
# else:
#     print('Число', number, 'не содержит цифру 7')

# while True:
#     if условие 1:  # условие для остановки цикла
#         break
#     ...
#     if условие 2:  # еще одно условие для остановки цикла
#         break
#     ...
#     if условие 3:  # еще одно условие для остановки цикла
#         break

# for i in range(1, 101):
#     if i == 7 or i == 17 or i == 29 or i == 78:
#         continue  # переходим на следующую итерацию
#     print(i)

# num = 1964
# while num != 0:
#     last_digit = num % 10
#     num //= 10

#     if last_digit % 3 == 0:
#         print(last_digit)
#         break
# num = 3281
# while num != 0:
#     print(num % 10, end='')
#     num //= 100
#     if num != 0:
#         continue
# for i in range(10):
#     print(i, end='*')
#     if i > 6:
#         break
# i = 100
# while i > 0:
#     if i == 40:
#         break
#     print(i, end='*')
# #     i -= 20
# n = 10
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue
#     print(n, end='*')
# result = 0
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     result += i
# print(result)
# mult = 1
# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#     if i % 9 == 0:
#         break
#     mult *= i
# print(mult)
# print('Наименьший делитель')
# num = int(input())
# for i in range(2, num + 1):
#     if num % i == 0:
#         break
# print(i)

# print('Следуй правилам')
# num = int(input())
# for i in range(1, num + 1):
#     if 5 <= i <= 9:
#         continue
#     if 17 <= i <= 37:
#         continue
#     if 78 <= i <= 87:
#         continue
#     print(i)
# n = 5
# while n > 0:
#     n -= 1
#     print(n)
# else:
# #     print('Цикл завершен.')
# num = int(input())
# n = num
# flag = False
# while n != 0:
#     last = n % 10
#     if last == 7:
#         flag = True
#         break        # прерываем цикл, так как число гарантированно содержит цифру 7
#     n //= 10

# if flag == True:
#     print('Число', num, 'содержит цифру 7')
# else:
# #     print('Число', num, 'не содержит цифру 7')
# num = int(input())
# n = num
# while n != 0:
#     last = n % 10
#     if last == 7:
#         print('Число', num, 'содержит цифру 7')
#         break
#     n //= 10
# else:
#     print('Число', num, 'не содержит цифру 7')
# num = 3
# while num < 8:
#     num += 1
# else:
#     print('Цикл завершен.')

# print(num)
# num = 3
# total = 0
# for i in range(num):
#     if i % 2 == i:
#         total += 1
# else:
#     print(total)

# print(total + 1)
# num = 4
# while num < 10:
#     num += 2
#     print(num)
# else:
#     print('Цикл завершен.')
# num = 7
# while num < 12:
#     num += 2
#     if num == 11:
#         break
#     print(num)
# else:
#     print('Цикл завершен.')
# num = 2
# while True:
#     num += 1
#     if num >= 5:
#         break
#     print(num)
# else:
#     print('Цикл завершен.')
# for i in range(5):
#     print(str(i) * 2)
#     if i >= 2:
#         break
# Производительность кода
# num = int(input())
# flag = True

# for i in range(2, num):
#     if num % i == 0:
#         flag = False

# if num == 1:
#     print('Число равно 1')
# elif flag == True:
#     print('Число простое')
# else:
#     print('Число составное')
# # better
# num = int(input())
# flag = True

# for i in range(2, num // 2 + 1):
#     if num % i == 0:
#         flag = False

# if num == 1:
#     print('Число равно 1')
# elif flag == True:
#     print('Число простое')
# else:
#     print('Число составное')
# # better 
# num = int(input())
# flag = True

# for i in range(2, int(num ** 0.5) + 1):
#     if num % i == 0:
#         flag = False

# if num == 1:
#     print('Число равно 1')
# elif flag == True:
#     print('Число простое')
# else:
#     print('Число составное')
# n = int(input())
# while n > 10:
#     n //= 10
# print(n)
# s = 0
# for i in range(7):
#     n = int(input())
#     if n % 2 == 0:
#         s = s + n
# print(s)

# n = int(input())
# max_digit = -1
# while n > 0:
#     digit = n % 10
#     if digit % 3 == 0:
#         if digit > max_digit:
#             max_digit = digit
#     n = n // 10
# if max_digit == -1:
#     print('NO')
# else:
#     print(max_digit)

# s = input()
# while len(s) < 10:
#     if len(s) % 4 == 0:
#         s = s + 'x'
#     elif len(s) % 5 == 0:
#         s = s + 'y'
#     else:
#         s = 'z' + s  
# s = '@' + s
# print(s)
# #  eleven  -  @zzzelevenx
# #  mike  -  @zzzmikexyx

# print('Цифровые сообщения')
# num = int(input())
# cnt = 0
# total = 1
# while num % 100 != 11:
#     if len(str(num)) > 7:
#         cnt += 1
#     total += 1
#     num = int(input())    
# if len(str(num)) > 7:
#     cnt += 1    
# print(cnt, '/', total, sep='')

# print('Ревью кода-6 🌶️🌶️')
# mx = -100001
# s = 0
# for i in range(10):
#     x = int(input())
#     if x < 0:
#         s += x
#         if x > mx:
#             mx = x
# if s < 0:            
#     print(s)
#     print(mx)
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
# num = int(input())
# for i in range (num):
# #    for j in range(3):
#     print(num, num, num )

# print('Таблица-2')
# num = int(input())
# for i in range (1, num + 1):
#     print(i, i, i, i, i )

print('Таблица-3')