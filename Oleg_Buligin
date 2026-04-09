# print('Предположим, что мы сделали вклад в банке с ежегодной капитализацией. На какую сумму вклад будет прирастать каждый год?')
# money = 100000  # Начальная сумма денег
# year = 0        # Счетчик лет
# yearly_multiplier = 0.05  # Процентная ставка (5%)
# money_target = money * 2  # Целевая сумма (в два раза больше)
# print(f'Стартовый капитал: {money:.2f} у.е.')
# while money < money_target:
#     # 1. Сначала считаем, сколько составит прирост в этом году
#     # (5% от текущей суммы)
#     growth = money * yearly_multiplier
#     # 2. Затем добавляем этот прирост к основной сумме
#     money += growth
#     money = money + growth
#     # 3. Увеличиваем счетчик лет
#     year += 1
#     print(f'Год {year}: {money:.2f} у.е. → прирост: {growth:.2f} у.е.')
# print(f'\nЦель в {money_target:.2f} у.е. достигнута за {year} лет.')
# print(f'Итоговый капитал: {money:.2f} у.е.')


# print('''Итерация по вложенным спискам''')
# print('''Задача: Обработка статусов серверов. У нас есть список пар [Имя сервера, Нагрузка CPU].''')
# # Список списков: [Server_Name, CPU_Load_%]
# server_stats = [
#     ['Server-A', 12],
#     ['Server-B', 85],
#     ['Server-C', 44],
#     ['Database-Prod', 92]
# ]
# print("🖥️ Мониторинг нагрузки:\n")
# for info in server_stats:
#     # print(info)
#     status = "OK 🟢"
#     if info[1] > 80:
#         status = "OVERLOAD 🔥"
#     print(f"Хост: {info[0]} | CPU: {info[1]}% | Статус: {status}")
# print(info)


# print('Напишем программу, которая последовательно запрашивает ' \
# 'у пользователя числа (по одному за раз) и после первого нуля выводит сумму всех ранее введенных чисел.')
# sum_ = 0
# number = 1
# while number != 0:
#     number = int(input("Введите число: "))
#     sum_ += number
# print(f"Сумма чисел равна: {sum_}")


# print('У нас есть список сумм транзакций. Нам нужно отфильтровать подозрительно крупные переводы для финмониторинга.')
# transactions = [50, 1200, 35, 7000, 150, 9990, 40]
# limit = 1000
# print(f"🔍 Анализ транзакций выше {limit}$:\n")
# for amount in transactions:
#     if amount > limit:
#         print(f"⚠️ ALARM: Обнаружена крупная транзакция: {amount}$")



# print('''The Pythonic Way: Функция enumerate()''')
# print('''Представьте задачу: у нас есть список задач (Sprint Backlog), 
#       и нам нужно вывести их на экран с порядковыми номерами.Как делает новичок (C/Java style): 
#       Создает отдельную переменную-счетчик и вручную увеличивает её.''')
# print(list(enumerate(['a', 'b', 'c'])))

# # ❌ Anti-pattern: Ручное управление индексом
# tasks = ['Fix Login Bug', 'Code Review', 'Deploy to Prod']
# i = 1
# for task in tasks:
#     print(f"{i}. {task}")
#     i += 1

# # ✅ Pythonic Way: Автоматическая нумерация
# project_roadmap = [
#     "Настройка окружения (Env)",
#     "Разработка API",
#     "Написание тестов",
#     "Релиз v1.0"
# ]

# print("📅 План работ на неделю:\n")
# # start=1 позволяет начать нумерацию с 1, а не с 0 (как принято у людей)
# for number, stage in enumerate(project_roadmap, start=1):
#     print(f"Этап {number}: {stage}")
# print(f"\nВсего этапов: {len(project_roadmap)}")


# print('Посчитаем сумму элементов по главной диагонали квадратной матрицы')
# data = [
#     [13, 25, 23, 34],
#     [45, 32, 44, 47],
#     [12, 33, 23, 95],
#     [13, 53, 34, 35]
# ]
# sum_ = 0
# for row in data:
#     print(row)
#     sum_ += row[3]
# print(f"Сумма элементов: {sum_}")

# Сырые данные с датчика.
# Могут содержать мусор ("ERROR", ""), полезные числа или сигнал аварии.
# sensor_readings = [
#     "24.5", "25.1", "", "ERROR", "26.0",
#     "CRITICAL_STOP", "28.5", "30.0"
# ]
# print("📊 Начинаем обработку данных сенсоров...\n")
# valid_count = 0
# total_temp = 0
# for reading in sensor_readings:
#     # 1. ПРОВЕРКА НА BREAK: Экстренная ситуация
#     # Если мы видим сигнал остановки, мы должны немедленно прекратить чтение
#     if reading == "CRITICAL_STOP":
#         print(f"\n📛 АВАРИЯ: Получен сигнал экстренной остановки системы!")
#         break
#     # 2. ПРОВЕРКА НА CONTINUE: Фильтрация мусора (Guard Clauses)
#     # Если данные пустые или это ошибка, мы не хотим их обрабатывать.
#     # continue позволяет пропустить этот шаг и не писать огромный if/else
#     elif reading == "" or reading == "ERROR":
#         print(f"⚠️ Сбой чтения: пропускаем некорректное значение '{reading}'")
#         continue
#     # Сюда мы попадаем только если данные корректны (не сработал ни break, ни continue).
#     current_temp = float(reading)
#     total_temp += current_temp
#     valid_count += 1
#     print(f"✅ Данные приняты: {current_temp}°C")
# print("-" * 30)
# if valid_count > 0:
#     print(f"Средняя температура: {total_temp / valid_count:.1f}°C")
# else:
#     print("Корректных данных не получено.")

# Сырые данные с датчика.
# Могут содержать мусор ("ERROR", ""), полезные числа или сигнал аварии.
# sensor_readings = [
#     "24.5", "25.1", "", "ERROR", "26.0",
#     "CRITICAL_STOP", "28.5", "30.0"
# ]
# print("📊 Начинаем обработку данных сенсоров...\n")
# valid_count = 0
# total_temp = 0
# for reading in sensor_readings:
#     # 1. ПРОВЕРКА НА BREAK: Экстренная ситуация
#     # Если мы видим сигнал остановки, мы должны немедленно прекратить чтение
#     if reading == "CRITICAL_STOP":
#         print(f"\n📛 АВАРИЯ: Получен сигнал экстренной остановки системы!")
#         break
#     # 2. ПРОВЕРКА НА CONTINUE: Фильтрация мусора (Guard Clauses)
#     # Если данные пустые или это ошибка, мы не хотим их обрабатывать.
#     # continue позволяет пропустить этот шаг и не писать огромный if/else
#     else:
#         try:
#             current_temp = float(reading)
#         except ValueError:
#             print(f"⚠️ Сбой чтения: пропускаем некорректное значение '{reading}'")
#             continue
#     # Сюда мы попадаем только если данные корректны (не сработал ни break, ни continue).
#     current_temp = float(reading)
#     total_temp += current_temp
#     valid_count += 1
#     print(f"✅ Данные приняты: {current_temp}°C")
# print("-" * 30)
# if valid_count > 0:
#     print(f"Средняя температура: {total_temp / valid_count:.1f}°C")
# else:
#     print("Корректных данных не получено.")

# import random
# number_to_guess = random.randint(1, 100)
# print(number_to_guess)
# tries_left = 3
# print(f"\nИгра 'Угадай число' (1-100), {tries_left} попытки:")
# while tries_left > 0:
#     print(f"  Осталось попыток: {tries_left}")
#     guess = int(input("  Ваш вариант: "))
#     if guess > number_to_guess:
#         print("  Загаданное число меньше.")
#     elif guess < number_to_guess:
#         print("  Загаданное число больше.")
#     else:
#         print("  Вы угадали! 🎉")
#         break # Выход из цикла по успеху
#     tries_left -= 1
# # Этот else сработает, если цикл завершился, т.к. tries_left стал 0
# # (т.е. break НЕ сработал - пользователь не угадал)
# else:
#     print(f"\nПопытки закончились! Вы не угадали.")
#     print(f"Было загадано число: {number_to_guess}")

# print('Выведем таблицу Пифагора:')
# for i in range(1, 10):
#     # print(i)
#     for j in range(1, 10):
#         print(f"{i} * {j} = {i * j}", end="\t")
#     print()
# for i in range(1, 10):
#     # print(i)
#     for j in range(1, 10):
#         print(f"{j} * {i} = {j * i}", end="\t")
#     print()

# # Структура данных: Список департаментов
# # Каждый элемент - это список: [Название отдела, [Сотрудник 1, Сотрудник 2, ...]]
# company_structure = [
#     ['Sales', ['John', 'Alice', 'Robert']],
#     ['Development', ['Oleg', 'Sarah', 'Dmitry', 'Linus']],
#     ['HR', ['Maria', 'Anna']]
# ]
# for dep, names in company_structure:
#     # print(dep, names)
#     print(f'{dep}:')
#     for name in names:
#         print(name)
#     print()