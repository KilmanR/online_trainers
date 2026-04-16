# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = {}  # У каждого студента СВОЙ словарь

# print('''Задания (Тема 1)
#       Создайте класс Book с атрибутами title, author, is_available = True. 
#       Создайте два объекта. У одного измените is_available на False. 
#       Выведите оба объекта через print(book.title, book.is_available). 
#       Убедитесь, что они независимы.
#       Добавьте в Book атрибут pages_read = []. 
#       Напишите метод read_page(page_num), который добавляет номер страницы в список. 
#       Проверьте, что у разных книг списки не пересекаются.
#       Создайте класс User с name и balance = 0. 
#       Напишите метод deposit(amount), который добавляет сумму к balance. 
#       Создайте двух пользователей, пополните им счета разными суммами, выведите итоги.''')

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.autthor = author
#         self.is_available = True
#         self.pages_read = []
#     def read_page(self, page_num):
#         if not isinstance (page_num, int) or page_num < 1:
#              return "Номер страницы должен быть целым положительным числом"
#         self.pages_read.append(page_num)
#         return None 

# book1 = Book("1984", "Джордж Оруэлл")
# book2 = Book("Война и мир", "Лев Толстой")
# book1.is_available = False
# book1.read_page(1)
# book1.read_page(2)
# book2.read_page(100)

# print(book1.pages_read)
# print(book2.pages_read)
# print(f"книга {book1.title}: прочитано {len(book1.pages_read)} стр. → {book1.pages_read}")
# print(f"книга {book2.title}: прочитано {len(book2.pages_read)} стр. → {book2.pages_read}")
# print(f"{book1.title} | Доступна: {book1.is_available}")
# print(f"{book2.title} | Доступна: {book2.is_available}")
# class User:
#     def __init__(self, name):
#         self.name = name
#         self.balance = 0.0
#         self.debt = 0.0
#     def deposit(self, amount):
#         if not isinstance(amount, (int, float)):
#             return 'Ошибка: сумма должна быть числом'
#         if amount <= 0:
#             return 'Ошибка: сумма должна быть больше нуля'
#         self.balance += amount
#         return None
#     def withdraw(self, amount):
#         if not isinstance(amount, (int, float)):
#             return 'Ошибка: сумма должна быть числом'
#         if amount <= 0:
#             return 'Ошибка: сумма должна быть больше нуля'                    
#         if amount > self.balance:
#             return 'Не достаточно средств'                    
#         self.balance -= amount        
#         return None


# user1 = User('Алиса')
# user2 = User('Борис')
# user1.deposit(1000)
# user2.deposit(500)
# user2.deposit(200)
# tatus1 = user1.withdraw(50)
# status2 = user1.withdraw(12.5)
# status3 = user2.withdraw(2000)
# print(f'{user1.name}: {user1.balance} руб. {status2 if status2 else "Успешно"}')
# print(f'{user2.name}: {user2.balance} руб. {status3 if status3 else "Успешно"}')
# print(f"{user1.name}: {user1.balance} руб.")
# print(f"{user2.name}: {user2.balance} руб.")

# class Bike:
#     def __init__(self, bike_id, model):
#         self.bike_id = bike_id
#         self.model = model
#         self.is_available = True
#         self.current_user = None
#     def rent(self, user_name):
#         if self.is_available:
#             self.is_available = False
#             self.current_user = user_name  # сохраняем переданную строку в атрибут
#             return None
#         return 'Велосипед уже арендован' 
#     def return_bike (self):
#         if not self.is_available:
#             self.is_available = True
#             self.current_user = None
#             return None
#         return 'Велосипед не был арендован'

# b1 = Bike('B001', 'Mountain')
# b2 = Bike('B002', 'City')

# print(b1.rent('Алексей'))      # Ожидаем: None
# print(b1.rent('Мария'))        # Ожидаем: 'Велосипед уже арендован'
# print(b1.return_bike())        # Ожидаем: None
# print(b1.return_bike())        # Ожидаем: 'Велосипед не был арендован'

# # Проверка независимости объектов
# b2.rent('Ольга')
# print(f"{b1.model}: занят? {not b1.is_available}")  # False
# print(f"{b2.model}: занят? {not b2.is_available}")  # True

# class PiggyBank:
#     def __init__ (self, owner_name):
#         self.owner_name = owner_name
#         self.balance = 0.0
#         self.history = []
#     def add(self, amount):
#         if not isinstance(amount, (int, float)) or amount <= 0:
#             return 'Ошибка: пополнение должно быть положительным числом'
#         self.balance += amount
#         self.history.append(f"Внесено: {amount}")
#         return None
#     def take(self, amount):
#         if not isinstance(amount, (int, float)) or amount <= 0:
#             return 'Ошибка: пополнение должно быть положительным числом'
#         if amount > self.balance:
#             return 'Недостаточно средств'
#         self.balance -= amount
#         self.history.append(f"Снято: {amount}")
#         return None
#     def show_history(self):
#         if not self.history:
#             return 'Операций нет'
#         return '\n'.join(self.history)    # !!! переводим список в строку и выводим каждую переменную на новой строке

# pb = PiggyBank('Дмитрий')

# print(pb.add(500))           # None
# print(pb.take(100))          # None
# print(pb.take(600))          # 'Недостаточно средств'
# print(pb.add(200))           # None

# print(f"Баланс: {pb.balance}")  # 600.0
# print(pb.show_history())

# print('ТЕМА 2: Наследование и super() (Подробная теория)')

# print('шпаргалка')
# class Parent:
#     def __init__(self, a):
#         self.a = a

# class Child(Parent):
#     def __init__(self, a, b):
#         super().__init__(a)  # ← Делегируем часть родителю
#         self.b = b           # ← Добавляем своё

# print('ЗАДАНИЕ 1: «Транспорт и его характеристики»')

# class Vehicle:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#     def get_info(self):
#         return f"Марка: {self.brand}, Модель: {self.model}, Год: {self.year}"

# class Car(Vehicle):
#     def __init__(self, brand, model, year, doors, fuel_type):
#         super().__init__(brand, model, year)
#         self.doors = doors
#         self.fuel_type = fuel_type
#     def get_info(self):
#         return super().get_info() + f" | Двери: {self.doors}, Топливо: {self.fuel_type}"

# class Bike(Vehicle):
#     def __init__(self, brand, model, year, bike_type, gears):
#         super().__init__(brand, model, year)
#         self.bike_type = bike_type
#         self.gears = gears
#     def get_info(self):
#         return super().get_info() + f" | Тип: {self.bike_type}, Скоростей: {self.gears}"
    
# c = Car("Toyota", "Camry", 2022, 4, "Бензин")
# b = Bike("Giant", "Talon", 2021, "Горный", 21)

# print(c.get_info())
# print(b.get_info())

# print(isinstance(c, Vehicle))  # True
# print(isinstance(b, Vehicle))  # True

# print('ЗАДАНИЕ 2: «Умные устройства»')

# class Device:
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power
#         self.is_on = False
#     def turn_on(self):
#         if not self.is_on:
#             self.is_on = True
#             return None
#         else:
#             return 'Устройство уже включено'
#     def turn_off(self):
#         if self.is_on:
#             self.is_on = False
#             return None
#         else:
#             return 'Устройство уже выключено'    
#     def get_status(self):
#         status = 'Включено' if self.is_on else 'Выключено'
#         return f"Устройство: {self.name}, Мощность: {self.power} Вт, Статус: {status}"
    
# # print('проверочный код на основной класс')
# # # 1. Создаём экземпляр
# # dev = Device("Ноутбук", 65)
# # # 2. Начальный статус
# # print(dev.get_status())  
# # # Ожидаем: Устройство: Ноутбук, Мощность: 65 Вт, Статус: Выключено
# # # 3. Включаем
# # print(dev.turn_on())     
# # # Ожидаем: None
# # print(dev.get_status())  
# # # Ожидаем: ... Статус: Включено
# # # 4. Пробуем включить повторно
# # print(dev.turn_on())     
# # # Ожидаем: Устройство уже включено
# # # 5. Выключаем
# # print(dev.turn_off())    
# # # Ожидаем: None
# # print(dev.get_status())  
# # # Ожидаем: ... Статус: Выключено
# # # 6. Пробуем выключить повторно
# # print(dev.turn_off())    
# # # Ожидаем: Устройство уже выключено
# class Smartphone(Device):
#     def __init__(self, name, power, storage_gb):
#         self.storage_gb = storage_gb
#         super().__init__(name, power)
#         self.apps = []
#     def get_status(self):
#         return super().get_status() + f" | Память: {self.storage_gb} ГБ, Приложений: {len(self.apps)}"
#     def install_app(self, app_name):
#         if not self.is_on:
#             return 'Ошибка: включите устройство'            
#         if not isinstance(app_name, str) or len(app_name) == 0: # проверяем чтобы апп_наме была строкой и длинной больше 0
#             return 'Ошибка: некорректное имя приложения'            
#         if app_name in self.apps:
#             return 'Приложение уже установлено'            
#         self.apps.append(app_name)      # добавляем апп в список установленных
#         return None

# class SmartWatch(Device):
#     def __init__(self, name, power, battery_hours):
#         super().__init__(name, power)
#         self.battery_hours = battery_hours
#     def get_status(self):
#         return super().get_status() + f" | Батарея: {self.battery_hours} ч"
#     def track_heartbeat(self):
#         if not self.is_on:
#             return 'Ошибка: включите устройство'
#         self.battery_hours -= 0.5
#         if self.battery_hours < 0:
#             self.battery_hours = 0.0
#         return f"Пульс: 72 уд/мин. Батарея после измерения: {self.battery_hours} ч"
# print('\n=== ЗАДАНИЕ 2: Проверка ===')

# phone = Smartphone("iPhone 15", 5, 256)
# watch = SmartWatch("Apple Watch", 2, 18)

# print(phone.get_status())
# print(phone.install_app("Telegram"))  # Ошибка: включите устройство

# phone.turn_on()
# print(phone.install_app("Telegram"))  # None
# print(phone.install_app("Telegram"))  # Приложение уже установлено

# print(watch.get_status())
# watch.turn_on()
# print(watch.track_heartbeat())        # Пульс: 72 уд/мин. Батарея после измерения: 17.5 ч
# print(watch.track_heartbeat())        # Пульс: 72 уд/мин. Батарея после измерения: 17.0 ч

# print(isinstance(phone, Device))      # True
# print(isinstance(watch, Device))      # True