import sqlite3

conn = sqlite3.connect('chinook.db')
cursor = conn.cursor()

query = """
SELECT g.Name, SUM(t.UnitPrice) as total_price
FROM Track t
JOIN Genre g ON t.GenreId = g.GenreId
GROUP BY g.Name
ORDER BY total_price DESC
LIMIT 10;
"""

cursor.execute(query)
results = cursor.fetchall()

# Способ 1: Сохранить в текстовый файл
with open('results2.txt', 'w', encoding='utf-8') as f:
    f.write(f"Всего исполнителей: {len(results)}\n\n")
    for row in results:
        f.write(f"{row[0]}\n")

print(f"✅ Результаты сохранены в results.txt")
print(f"📊 Всего: {len(results)} исполнителей\n")

# Показать первые 10
print("Первые 10:")
for i, row in enumerate(results[:10], 1):
    print(f"  {i}. {row[0]}")

conn.close()