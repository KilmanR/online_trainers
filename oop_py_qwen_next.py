# print('''ТЕМА 3: Композиция, @classmethod, @staticmethod и агрегация данных''')
# print('примеры')
# class Engine:
#     def start(self):
#         return "Вжжж!"
# class Car:
#     def __init__(self):
#         # Машина НЕ является двигателем. Она ИМЕЕТ двигатель.
#         self.engine = Engine()  # ← Композиция        
#     def drive(self):
#         print(self.engine.start())
# c = Car()
# c.drive()  # Вжжж!

# class Validator:
#     @staticmethod
#     def is_valid_score(score):
#         # Не использует self. Работает только с переданным аргументом
#         return isinstance(score, (int, float)) and 1 <= score <= 10
# # Вызываем БЕЗ создания объекта Validator()
# print(Validator.is_valid_score(7))   # True
# print(Validator.is_valid_score(15))  # False
# print(Validator.is_valid_score("а")) # False

# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#     @classmethod
#     def from_csv_line(cls, line):
#         # line = "Анна; anna@mail.ru"
#         name, email = line.split("; ")
#         return cls(name, email)  # cls(...) == User(...)
# # Обычное создание:
# u1 = User("Борис", "boris@mail.ru")
# # Создание из строки через классовый метод:
# u2 = User.from_csv_line("Вика; vika@mail.ru")
# print(u2.name, u2.email)  # Вика vika@mail.ru

# class Player:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
# players = [Player("А", 10), Player("Б", 5), Player("В", 8)]
# # 1. Найти объект с максимальным score:
# best = max(players, key=lambda p: p.score)
# print(best.name)  # А
# # 2. Посчитать среднее арифметическое:
# total = sum(p.score for p in players)
# avg = total / len(players) if players else 0.0
# print(f"{avg:.1f}")  # 7.7

# class Box:
#     def __init__(self, size): self.size = size    
#     @staticmethod
#     def is_fit(item_size, box_size):
#         return item_size <= box_size        
#     @classmethod
#     def from_dimensions(cls, h, w, d):
#         return cls(h * w * d)
# b = Box(100)
# print(Box.is_fit(50, b.size))  # True (вызов без объекта)
# print(b.is_fit(150, b.size))   # True (можно и через объект)
# b2 = Box.from_dimensions(2, 3, 4)
# print(b2.size)                 # 24 (cls() создал новый объект)

