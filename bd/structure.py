import sqlite3

conn = sqlite3.connect('chinook.db')
cursor = conn.cursor()

# Получаем все таблицы
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("📊 СТРУКТУРА БАЗЫ ДАННЫХ:\n")

for table in tables:
    table_name = table[0]
    print(f"\n📁 Таблица: {table_name}")
    print("-" * 50)
    
    # Получаем информацию о колонках
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    
    for col in columns:
        # col[1] - имя, col[2] - тип, col[3] - NOT NULL, col[4] - PK
        not_null = "NOT NULL" if col[3] else ""
        pk = "🔑 PRIMARY KEY" if col[5] else ""
        print(f"  {col[1]:20} {col[2]:15} {not_null:10} {pk}")

conn.close()