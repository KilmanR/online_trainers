# 📦 Необходимый софт

Список всех программ и инструментов, которые понадобятся для настройки.

## 🔽 Что нужно скачать

### 1. Для установки Ubuntu

#### Rufus (для создания загрузочной флешки)
- **Сайт**: [rufus.ie](https://rufus.ie/ru/)
- **Размер**: ~1.5 MB
- **Зачем**: Создание загрузочной USB-флешки с Ubuntu

#### Ubuntu 26.04 LTS
- **Сайт**: [ubuntu.com/download/desktop](https://ubuntu.com/download/desktop)
- **Размер**: ~3-4 GB
- **Зачем**: Операционная система Linux

---

### 2. Для Windows

#### Python 3.12
- **Сайт**: [python.org/downloads](https://www.python.org/downloads/)
- **Версия**: 3.12.x (последняя стабильная)
- **Размер**: ~25 MB
- **Зачем**: Язык программирования Python

#### Visual Studio Code
- **Сайт**: [code.visualstudio.com](https://code.visualstudio.com/)
- **Размер**: ~90 MB
- **Зачем**: Редактор кода

#### Git для Windows
- **Сайт**: [git-scm.com/download/win](https://git-scm.com/download/win)
- **Размер**: ~50 MB
- **Зачем**: Система контроля версий

---

### 3. Для Ubuntu

Все необходимое устанавливается через терминал:

```bash
# Обновление системы
sudo apt update
sudo apt upgrade -y

# Git
sudo apt install -y git

# Python (обычно уже установлен)
python3 --version

# VS Code
sudo snap install code --classic