# start = 15   # вывести первые 8 нечётных чисел, начиная с 15
# for i in range(8):
#     num = start + i * 2
#     print(num)

# for i in range(50, 9, -1):  # считать назад от 50 до 10, показывая только числа, кратные 5
#     if i % 5 != 0:
#         continue
#     print (i)

# product = 1  # вычислить и вывести произведения всех чисел от 1 до 30 (включительно), кратных 3
# for i in range(1, 31):
#     if i % 3 == 0:
#         product = product * i
# print(product)

# rows = int(input())  # рисуем звездочки прямоугольник
# cols = int(input())
# for i in range(rows):
#     row = ""
#     for j in range(cols):
#         row += "*"
#     print(row)

# n = int(input())
# #while True:
# for i in range(1, (n + 1)):
#     for j in range(1 , n + 1):
#         if i * j == n:
#             print(i, j)
        
# def print_large_number():
#     print('50005000')
# n = int(input())
# for i in range(n):

#     print_large_number()




# input_num = int(input())
# def square_number(n):
#     result = n * n
#     print(result)
# square_number(input_num)

# def cube_number(n):
#     result = n ** 3
#     print(result)   
# num = int(input())
# cube_number(num)
# def cube_number(n):
#     cube = n ** 3
#     return cube
# input_num = int(input())
# result = cube_number(input_num)
# print(result)
# def sum_to_n(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += i
#     return total


# n = int(input())
# def sigma(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += i
#     print(total)
# sigma(n)

# def is_valid(username, password):
#     if username == 'admin' or (username == 'user' and password = 'qweasd'):
#         return True
#     else:
#         return False

# print('Welcome to FizzBuzz!') # игра FizzBuzz много уроков, пишу всё за раз

# def fizzbuzz(number):
#     result = ''
#     if number % 3 == 0:
#         result += 'Fizz'
#     if number % 7 == 0:
#         result += 'Buzz'
#     if result == '':
#         if '3' in str(number):
#             result = 'Almost Fizz'
#         else: 
#             result = str(number)
#     return result
# limit = int(input())
# for i in range(1, limit +1):
#     print(fizzbuzz(i))

# def change_element(lst, index, new_element):
#     lst[index] = new_element
#     print(lst)
# lst = ['a', 'b', 'c']
# index = 1
# new_element = 'd'
# change_element(lst, index, new_element)

# def change_element(lst1, index, lst2):
#     lst1[index] = lst2[index - 1]
#     print(lst1)
# lst1 = [1, 2, 3]
# index = 1
# lst2 = [5, 6, 7]
# change_element(lst1, index, lst2)

# lst1 = [1, 2, 3]
# lst2 = [3, 4, 5]
# result = []
# def merge(lst1, lst2):
#     for element in lst1:
#         result.append(element)
#     for element in lst2:
#         result.append(element)
#     result.sort()
#     print(result)
# merge( lst1, lst2)

# def combine_and_filter(lst, threshold):
#     filtered_numbers = [num for num in lst if num > threshold]
#     filtered_numbers.sort()
#     print(filtered_numbers)
#     return filtered_numbers        
    

# lst = [1, 5, 3, 8, 2, 7, 4, 6]
# threshold = 4
# combine_and_filter(lst, threshold)

# def prod(lst):
#     product = 1
#     for num in lst:
#         product *= num
#     print(product)
#     return product
    
# def reverse(lst):
#     reversed_list = []
#     for i in range(len(lst) - 1, -1, -1):
#         reversed_list.append(lst[i])
#     return reversed_list


# lst = [1, 2, 3]
# prod(lst)

# print('способ перебора списка с использованием for')

# fruits = ['apple', 'banana', 'orange']  # выводим весь список на каждой строке каждый элемент
# for fruit in fruits:
#     print(fruit)

# fruits = ['apple', 'banana', 'orange']    # сортируем по длине элементов списка
# for fruit in fruits:
#     if len(fruit) > 5:
#         print(fruit)

# print('Создайте программу, которая получает список как ввод (данный), ' \
# 'и выводит новый список, содержащий только слова длиннее чем 5 символов')

# lst = input().split(',')
# lst1 = []
# for i in lst:
#     if len(i) > 5:
#         lst1.append(i)
# print(lst1)

# print('сумма элементов списка')
# numbers = input().split(',')  # вводим строку
# even_sum = 0                        
# for num in numbers:
#     if int(num) % 2 == 0:   
#         even_sum += int(num)
# print(even_sum)

# print('перебор последовательности')
# fruits = ['apple', 'banana', 'orange']
# for i in range(len(fruits)):
#     print(f'index {i}: {fruits[i]}')

# print('перебор последовательности через enumerate()')
# fruits = ['apple', 'banana', 'orange']
# for index, fruit in enumerate(fruits):
#     print(f'Index {index}: {fruit}')

# lst = list(map(int, input().split(',')))
# lst1 = []
# for index, num in enumerate(lst):
#     if num <= 50 or num % 5 == 0:
#         lst1.append(index)
# print(lst1)    

# lst = ('cat', 'apple',  'dog', 'elephant', 'ant')
# #lst = input().split()
# lst1 = []
# for index, value in enumerate(lst):
#     if len(value) > 3 or value.startswith('a'):
#         lst1.append(index)
# print(lst1)

# text = 'Hey'
# for char in text:
#     print(char)
# for i in range(len(text)):
#     print(f'position {i}: {text[i]}')

# print('Создайте программу, которая получает строку как ввод, ' \
# 'и она печатает, сколько раз символ  (или P) встречается в строке.p')

# text = input()
# count = text.lower().count('p')
# print(count)

# print('создаём список из строки')
# text = 'apple banana cherry'
# fruits = text.split()         # разделение по пробелам
# print(fruits)

# data = 'john, 25, new york'
# data = data.split(',')          # разделение по запятой
# print(data)

# print('обьединяем список в строку')

# words = ['Hello', 'World', 'Python']
# text = ' '.join(words)                  # соединяем через пробел
# print(text)

# fruits = ['apple', 'banana', 'cherry']
# line = ','.join(fruits)                 # соединяем через запятую
# print(line)

# text = input()
# delimiter = input()
# t = text.split()
# new_t = delimiter.join(t)
# print(new_t)

# numbers = input()
# prefix = input()

# num = numbers.split()

# def add_prefix(num):
#     return prefix + num
# auto_prefix = [add_prefix(num) for i in num]
# print(auto_prefix)

# num = input()
# pref = input()
# num_list = num.split()
# mod_num = [pref + i for i in num_list]
# result = ' '.join(mod_num)
# print(result)

# lst = input().split(',')
# def get_slice(lst):
#     length = len(lst)
#     if length == 0:
#         return[]
#     if length % 2 == 1:
#         mid_index = length // 2
#         start = max(0, mid_index - 1)
#         end = min(length,mid_index + 2)
#         return lst[start:end]
#     else:
#         mid_index = length // 2
#         return lst[mid_index - 1: mid_index + 1]
# result = get_slice(lst)
# print(result)

# red,orange,yellow.green,blue,purple,pink,brown,black,white,gray,violet,indigo,maroon,navy
# print('срезы сисков')
# lst = input().split(',')
# lst1 = lst[1::3]
# lst2 = lst[5::-1]
# st = len(lst) // 2
# lst3 = lst[st::2]
# print(lst1)
# print(lst2)
# print(lst3)

# 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
# original_list = input().split(',')
# list1 = original_list[2::4]
# list2 = original_list[2:-2]
# list3 = original_list[-1::-2]
# list4 = original_list[:3] + original_list[-3:]
# print('List 1:', list1) # ['3', '7', '11', '15']
# print('List 2:', list2) # ['3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
# print('List 3:', list3) # ['15', '13', '11', '9', '7', '5', '3', '1']
# print('List 4:', list4) # ['1', '2', '3', '13', '14', '15']

# numbers = [1, 2, 3]
# repeats = 2
# def create_pattern(numbers, repeats):
#     num_new = numbers + numbers
#     num_new = num_new * repeats
#     return
# create_pattern(numbers, repeats)

# numbers = input().split()
# part1 = numbers + numbers[::-1]
# first_element = numbers[0] if numbers else None
# last_element = numbers[-1] if numbers else None
# part2 = [first_element] + part1 + [last_element]
# final_result = part2 * 2
# print(final_result)

# print("Welcome to the Daily Expense Tracker!")

# # Отобразить меню один раз
# print("\nMenu:")
# print("1. Add a new expense")
# print("2. View all expenses")
# print("3. Calculate total and average expense")
# print("4. Clear all expenses")
# print("5. Exit")

# # Инициализировать пустой список для хранения расходов
# expenses = []

# while True:
#     # Получить выбор пользователя
#     choice = input()
    
#     if choice == "1":
#         # Добавить новый расход
#         amount = float(input())
#         expenses.append(amount)
#         print("Expense added successfully!")

#     elif choice == "2":
#         # Просмотреть все расходы
#         if len(expenses) == 0:
#             print("No expenses recorded yet.")
#         else:
#             print("Your expenses:")
#             for i in range(len(expenses)):
#                 print(f"{i + 1}. {expenses[i]}")

#     elif choice == "3":
#         # Рассчитать общую и среднюю сумму расходов
#         if len(expenses) == 0:
#             print("No expenses recorded yet.")
#         else:
#             total = 0
#             for expense in expenses:
#                 total += expense
#             average = total / len(expenses)
#             print(f"Total expense: {total}")
#             print(f"Average expense: {average}")

#     elif choice == "4":
#         # Очистить все расходы
#         expenses = []
#         print("All expenses cleared.")

#     elif choice == "5":
#         # Выйти из программы
#         print("Exiting the Daily Expense Tracker. Goodbye!")
#         break

# print('пирамида звёздочек')
# n = int(input())
# for i in range(1, n + 1, 2):
#     if n / 2 != 0:
#         print('*' * i)

# def find_occurrences(text, pattern):
#     if not pattern:
#         return(False, 0, [])
#     occurrences = []
#     start = 0
#     while True:
#         pos = text.find(pattern, start)
#         if pos == -1:
#             break
#         occurrences.append(pos)
#         start = pos + 1
#         count = len(occurrences)
#     found = count > 0
#     return(found, count, occurrences)
#     pass

# # Чтение ввода
# text = input()
# pattern = input()

# # Вызов вашей функции и вывод результата
# result = find_occurrences(text, pattern)
# print(result)

# print('что купить')

# prices = input().split(',')
# for i in range(len(prices)):
#     prices[i] = int(prices[i])

# items = input().split(',')
# budget_per_item = int(input())
# affordable_items = []
# cant_afford = 0
# total_needed = 0

# for i in range(len(prices)):
#     if prices[i] <= budget_per_item:
#         affordable_items.append(items[i])
#         total_needed += prices[i]
#     else:
#         cant_afford += 1