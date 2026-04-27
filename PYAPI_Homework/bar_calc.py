import sys

# Глобальный словарь рецептов
cocktail_recipes = {}

def load_cocktails(filename="cocktails.txt"):
    """Загружает рецепты из txt-файла в глобальный словарь."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                recipe_name = line.strip()
                if not recipe_name:
                    continue

                count = int(next(f).strip())
                ingredients = []
                for _ in range(count):
                    ing_line = next(f).strip()
                    name, qty, measure = [part.strip() for part in ing_line.split("|")]
                    ingredients.append({
                        "ingredient_name": name,
                        "quantity": float(qty),
                        "measure": measure
                    })
                cocktail_recipes[recipe_name] = ingredients
    except FileNotFoundError:
        print("❌ Ошибка: файл cocktails.txt не найден рядом с программой!")
        sys.exit(1)

def get_shop_list_by_drinks(drinks, person_count):
    """Возвращает словарь ингредиентов с суммарными количествами."""
    shop_list = {}
    for drink in drinks:
        # Ищем название без учёта регистра
        match = next((name for name in cocktail_recipes if name.lower() == drink.lower()), None)
        if not match:
            continue

        for ing in cocktail_recipes[match]:
            name = ing["ingredient_name"]
            qty = ing["quantity"] * person_count
            measure = ing["measure"]

            if name in shop_list:
                shop_list[name]["quantity"] += qty  # ✅ Суммируем повторы
            else:
                shop_list[name] = {"measure": measure, "quantity": qty}
                
    return shop_list

def main():
    print("🍹 Коктейльный калькулятор\n")
    load_cocktails()

    available = list(cocktail_recipes.keys())
    print(f"📖 В наличии: {', '.join(available)}\n")

    # Запрос коктейлей
    drinks_input = input("🍸 Введите коктейли через запятую: ").strip()
    if not drinks_input:
        print("👋 Ничего не выбрано.")
        input("Нажмите Enter для выхода...")
        return

    drinks = [d.strip() for d in drinks_input.split(",") if d.strip()]

    # Запрос персон
    try:
        person_count = int(input("👥 Количество персон: ").strip())
    except ValueError:
        print("❌ Введите целое число!")
        input("Нажмите Enter для выхода...")
        return

    # Расчёт
    shop_list = get_shop_list_by_drinks(drinks, person_count)

    if not shop_list:
        print("❌ Ни один коктейль не найден. Проверьте названия.")
    else:
        print("\n🛒 Список закупки:")
        for name, data in shop_list.items():
            print(f"  • {name}: {data['quantity']} {data['measure']}")

    input("\n👉 Нажмите Enter для выхода...")

if __name__ == "__main__":
    main()