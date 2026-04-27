print('Шпаргалки')
print('=' * 20)

# Запись одной строки
with open('hello.txt', 'w', encoding='utf-8') as f:
    f.write('Привет, файл!\n')

# Запись нескольких строк
with open('hello.txt', 'w', encoding='utf-8') as f:
    f.write('Первая строка\n')
    f.write('Вторая строка\n')
    f.write('Третья строка\n')

# 1. Читаем всё содержимое как одну большую строку
with open('hello.txt', 'r', encoding='utf-8') as f:
    content = f.read()
print(content)

# 2. Читаем построчно (самый экономный по памяти способ)
with open('hello.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(f'📄 {line.strip()}')  # .strip() убирает лишний \n и пробелы

# 3. Читаем все строки в список
with open('hello.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()  # ['Первая строка\n', 'Вторая строка\n', ...]
print(lines)

with open('hello.txt', 'a', encoding='utf-8') as f:  # Добавление в конец файла (без перезаписи)
    f.write('Эта строка добавлена позже.\n')

FILENAME = 'notes.txt'

# 1. Создаём/перезаписываем файл
with open(FILENAME, 'w', encoding='utf-8') as f:
    f.write('Купить молоко\n')
    f.write('Позвонить маме\n')
    f.write('Закончить проект\n')

# 2. Читаем и фильтруем строки
with open(FILENAME, 'r', encoding='utf-8') as f:
    important = [line.strip() for line in f if 'проект' in line.lower()]

print('Важные задачи:', important)
# Вывод: Важные задачи: ['Закончить проект']    

# Если файла нет → создастся. Если есть → полностью перезапишется
with open('my_file.txt', 'w', encoding='utf-8') as f:
    f.write('Первый текст\n')

try:
    with open('new_data.txt', 'x', encoding='utf-8') as f: # создаст файл если его нету
        f.write('Создан впервые!\n')
    print('✅ Файл создан')
except FileExistsError:
    print('⚠️ Такой файл уже существует')           # если есть, выдаст ошибку

print('создаём папки и файлы')
from pathlib import Path
# Полный путь к файлу (папки + имя файла)
file_path = Path("data/reports/2026/april/summary.txt")
# 1️⃣ Создаём все папки по пути автоматически
file_path.parent.mkdir(parents=True, exist_ok=True)
# 2️⃣ Пишем в файл
with file_path.open("w", encoding="utf-8") as f:
    f.write("Отчёт за апрель 2026\n")
    f.write("Статус: готово\n")
print(f"✅ Файл создан: {file_path}")

import os
dir_path = "data/reports/2026/april"
file_path = os.path.join(dir_path, "summary.txt")
# Создаём папки
os.makedirs(dir_path, exist_ok=True)
# Пишем в файл
with open(file_path, "w", encoding="utf-8") as f:
    f.write("Альтернативный вариант через os\n")

from pathlib import Path
def save_to_file(text: str, relative_path: str) -> None:
    path = Path(relative_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(f"📄 Сохранено: {path.absolute()}")
# Использование:
save_to_file("Купить молоко\nПозвонить маме\n", "lists/todo_2026.txt")
save_to_file("Лог инициализации...\n", "logs/app/debug.log")