
---

## 📄 **Файл 5: `04-vscode-setup.md`**

```markdown
# 💻 Настройка Visual Studio Code

Установка и настройка редактора кода VS Code для Python-разработки.

## 📋 Содержание
1. [Установка VS Code](#установка-vs-code)
2. [Установка расширений](#установка-расширений)
3. [Настройка интерфейса](#настройка-интерфейса)
4. [Настройка Python](#настройка-python)
5. [Настройка темы](#настройка-темы)

---

## 1. Установка VS Code

### На Windows

#### Шаг 1: Скачивание

1. Перейдите на [code.visualstudio.com](https://code.visualstudio.com/)
2. Нажмите **"Download for Windows"**
3. Сохраните установщик

**[Место для скриншота сайта VS Code]**

#### Шаг 2: Установка

1. Запустите установщик
2. Примите лицензионное соглашение
3. ✅ Оставьте все галочки:
   - ☑️ Add "Open with Code" to context menu
   - ☑️ Register Code as editor for supported file types
4. Нажмите **"Next"** → **"Install"**

**[Место для скриншота установщика]**

#### Шаг 3: Запуск

1. Нажмите **"Finish"**
2. VS Code откроется автоматически

---

### На Ubuntu

#### Способ 1: Через Snap (рекомендуется)

```bash
sudo snap install code --classic


# Скачайте пакет
wget -O code.deb https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64

# Установите
sudo dpkg -i code.deb
sudo apt-get install -f

# Или добавьте репозиторий Microsoft
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
sudo sh -c 'echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt update
sudo apt install code