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

print('Максимум и минимум')
largest = 0
for _ in range(10):
    num = int(input())    
    if num > largest:
        largest = num
print('Наибольшее число равно', largest) 

largest = int(input())  # принимаем первое число за максимальное
for _ in range(9):
    num = int(input())
    if num > largest:
        largest = num
print('Наибольшее число равно', largest) 