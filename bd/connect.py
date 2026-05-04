import sqlite3

conn = sqlite3.connect('chinook.db')
cursor = conn.cursor()

# Получаем все таблицы
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("🔗 СВЯЗИ МЕЖДУ ТАБЛИЦАМИ:\n")

for table in tables:
    table_name = table[0]
    
    # Получаем внешние ключи для каждой таблицы
    cursor.execute(f"PRAGMA foreign_key_list({table_name})")
    fkeys = cursor.fetchall()
    
    if fkeys:
        print(f"\n📁 Таблица: {table_name}")
        for fk in fkeys:
            # fk[2] - откуда (таблица), fk[3] - какое поле, fk[4] - на какое поле
            print(f"  └─ {fk[3]} → {fk[2]}.{fk[4]}")

print("\n\n📊 СХЕМА СВЯЗЕЙ:")
print("=" * 60)

# Более наглядный вариант
for table in tables:
    table_name = table[0]
    cursor.execute(f"PRAGMA foreign_key_list({table_name})")
    fkeys = cursor.fetchall()
    
    for fk in fkeys:
        print(f"{table_name}.{fk[3]} → {fk[2]}.{fk[4]}")

conn.close()