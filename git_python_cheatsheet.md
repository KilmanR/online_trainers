# 🚀 Python + Git — шпаргалка (обновлённая версия, бывший cheatsheet.md)
#
# ⚠️ Файл разделён по ОС: всё для Linux/Ubuntu (текущая система) — в начале,
#     для Windows — отдельный блок «🪟 Windows» в самом низу.

## 🐍 Python venv (Linux / Ubuntu)

# Создание виртуального окружения в папке .venv
python3 -m venv .venv

# Активация (Linux / macOS)
source .venv/bin/activate

# Деактивация окружения
deactivate

# Удаление окружения (Linux / macOS)
rm -rf .venv

# Создать окружение с конкретной версией Python
python3.12 -m venv .venv

# Узнать текущий интерпретатор и версию
which python3
python3 --version

# Установка пакета / посмотреть установленные
python3 -m pip install <пакет>
python3 -m pip list          # = pip list
python3 -m pip show <пакет>  # детали пакета (версия, путь)

# Поднять простой HTTP-сервер в текущей папке (8000 порт)
python3 -m http.server

# Проверить код без запуска (в т.ч. неиспользуемые импорты)
python3 -m pyflakes <файл.py>

---

## 🌳 Git (команды одинаковы для Linux и Windows — в Git Bash)

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

# ─── Отмены и откаты ────────────────────────────────────

# Отозвать изменение из индекса (файл остаётся изменённым)
git reset HEAD <имя_файла>

# Отменить изменения в рабочем файле (вернуть из последнего коммита)
git restore <имя_файла>

# Отменить добавленный файл после git add . (вернуть в working dir)
git restore --staged <имя_файла>

# Спрятать текущие изменения на время
git stash
git stash pop        # вернуть обратно

# Изменить сообщение последнего коммита
git commit --amend -m "новое описание"

# Вернуть удалённый файл из коммита
git restore <файл> -- <путь>

# ─── Различия ───────────────────────────────────────────

# Показать изменения в рабочих файлах
git diff

# Показать, что попадёт в коммит (из индекса)
git diff --staged

# История изменений конкретного файла
git log -p -- <файл>

# Гораздо более читаемо (требуется внешняя утилита diff-so-fancy)
# git config --global core.pager "diff-so-fancy | less --tabs=4 -RF"

# ─── Удалённые репозитории ──────────────────────────────

# Посмотреть список remote (origin, gitverse в т.ч.)
git remote -v

# Добавить второй remote
git remote add gitverse <URL>

# ─── Теги ───────────────────────────────────────────────

# Создать тег (версию) на текущем коммите
git tag v1.0.0

# Отправить теги на remote
git push --tags

# Удалить тег локально и на remote
git tag -d v1.0.0
git push origin --delete v1.0.0

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

## ✅ Чеклист перед началом работы (Linux)

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

---

## 🪟 Windows (блок для Windows)

### Python venv (Windows)

# Создание окружения
python -m venv .venv

# Активация (PowerShell)
.venv\Scripts\Activate.ps1

# Активация (CMD)
.venv\Scripts\activate.bat

# Деактивация окружения
deactivate

# Удаление окружения
rmdir /s /q .venv

### Заметки для Windows

# .gitignore вместо touch:  type nul > .gitignore   (CMD)  /  New-Item .gitignore  (PowerShell)
# echo ".venv/" >> .gitignore — работает так же
# pip: python -m pip install <пакет>, python -m pip freeze > requirements.txt
# Создание venv на Windows: python -m venv .venv