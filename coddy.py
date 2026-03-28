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

print('Welcome to FizzBuzz!') # игра FizzBuzz много уроков, пишу всё за раз

def fizzbuzz(number):
    result = ''
    if number % 3 == 0:
        result += 'Fizz'
    if number % 7 == 0:
        result += 'Buzz'
    if result == '':
        if '3' in str(number):
            result = 'Almost Fizz'
        else: 
            result = str(number)
    return result
limit = int(input())
for i in range(1, limit +1):
    print(fizzbuzz(i))