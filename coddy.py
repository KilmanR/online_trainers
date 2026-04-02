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

