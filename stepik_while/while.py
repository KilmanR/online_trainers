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

print('Сколько ждать? ⏱️')
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

    
