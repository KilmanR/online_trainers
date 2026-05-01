import os

FOLDER = "certificate"

# Показываем что будет удалено
print("Будут удалены:")
for f in os.listdir(FOLDER):
    if "_opt.pdf" in f:
        print(f"  - {f}")

# Удаляем
confirm = input("\nУдалить? (y/n): ")
if confirm.lower() == 'y':
    for f in os.listdir(FOLDER):
        if "_opt.pdf" in f:
            os.remove(os.path.join(FOLDER, f))
            print(f"✅ Удалено: {f}")