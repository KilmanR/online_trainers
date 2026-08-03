## 🐍 Python venv

# Создание виртуального окружения в папке .venv
python3 -m venv .venv

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

# Делаем дубль на гитвёрс
git push origin && git push gitverse

# Пушим сразу на оба ресурса
git pushall

# ─── Ветки ──────────────────────────────────────────────

# Посмотреть список веток
git branch

# Создать новую ветку
git branch <имя_ветки>

# Переключиться на ветку
git checkout <имя_ветки>

# Создать и сразу переключиться (короткий путь)
git checkout -b <имя_ветки>

# Переименовать текущую ветку
git branch -m <новое_имя>

# Удалить ветку (локальную)
git branch -d <имя_ветки>

# Слить ветку в текущую
git merge <имя_ветки>

# Посмотреть удалённые ветки
git branch -r

# Удалить ветку на удалённом сервере
git push origin --delete <имя_ветки>

# ─── .gitignore ─────────────────────────────────────────

# Быстро создать .gitignore через GitHub
# https://www.toptal.com/developers/gitignore

# Или создать вручную
touch .gitignore

# Типичное содержимое для Python-проекта:
# .venv/              — виртуальное окружение
# __pycache__/        — кэш Python
# *.pyc               — скомпилированные файлы
# .env                — секреты и переменные окружения
# *.log               — лог-файлы
# dist/               — собранные пакеты
# build/              — директория сборки
# .idea/              — IDE JetBrains
# .vscode/            — VS Code

# Добавить паттерн в .gitignore
echo ".venv/" >> .gitignore
echo "__pycache__/" >> .gitignore

# Убрать уже отслеживаемый файл из Git (но оставить на диске)
git rm --cached <имя_файла>

# Убрать уже отслеживаемую папку
git rm -r --cached <папка>

# ─── requirements.txt ───────────────────────────────────

# Сохранить все установленные пакеты с версиями
pip freeze > requirements.txt

# Сохранить только явно установленные пакеты (без зависимостей)
pip freeze --exclude-editable > requirements.txt

# Установить все зависимости из файла
pip install -r requirements.txt

# Обновить все пакеты до последних версий
pip install --upgrade -r requirements.txt

# Проверить, есть ли устаревшие пакеты
pip list --outdated

# Обновить конкретный пакет
pip install --upgrade <пакет>

# Удалить ненужный пакет
pip uninstall <пакет>

# Показать дерево зависимостей (нужно: pip install pipdeptree)
pipdeptree

# ─── Best Practices ─────────────────────────────────────

# Разделять зависимости для разных окружений:
#   requirements.txt          — основные зависимости
#   requirements-dev.txt      — для разработки (тесты, линтеры)
#   requirements-prod.txt     — для продакшена

# Пример requirements-dev.txt:
# -r requirements.txt         — подключить основной файл
# pytest                      — тесты
# flake8                      — линтер
# black                       — форматирование

# Не коммитить .venv/ — только requirements.txt
# Не коммитить .env — только .env.example с шаблоном
# Всегда фиксировать версии (==1.2.3), не оставлять без версий
# Периодически обновлять зависимости: pip install --upgrade -r requirements.txt

---

## ✅ Чеклист перед началом работы

# 1. Создать папку проекта
mkdir <имя_проекта> && cd <имя_проекта>

# 2. Инициализировать Git
git init

# 3. Создать .gitignore
touch .gitignore
# (заполнить по списку выше)

# 4. Создать виртуальное окружение
python3 -m venv .venv

# 5. Активировать окружение
source .venv/bin/activate

# 6. Установить зависимости
pip install <пакеты>

# 7. Зафиксировать зависимости в файл
pip freeze > requirements.txt

# 8. Сделать первый коммит
git add .
git commit -m "init: структура проекта, venv, gitignore"

# 9. (Опционально) Создать ветку для разработки
git checkout -b dev