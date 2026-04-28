## 🐍 Python venv

# Создание виртуального окружения в папке .venv
python -m venv .venv

# Активация (Linux / macOS)
source .venv/bin/activate

# Активация (Windows PowerShell)
.venv\Scripts\Activate.ps1

# Активация (Windows CMD)
.venv\Scripts\activate.bat

# Деактивация окружения
deactivate

# Удаление окружения (Linux / macOS)
rm -rf .venv

# Удаление окружения (Windows)
rmdir /s /q .venv

---

## 🌳 Git

# Инициализация нового репозитория
git init

# Клонирование удалённого репозитория
git clone <URL_репозитория>

# Проверка статуса файлов
git status

# Добавление всех изменённых файлов в индекс
git add .

# Добавление конкретного файла в индекс
git add <имя_файла>

# Фиксация изменений с комментарием
git commit -m "описание изменений"

# Отправка изменений на удалённый сервер (ветка main)
git push origin main

# Получение и применение изменений с сервера
git pull

# История коммитов в компактном виде
git log --oneline
