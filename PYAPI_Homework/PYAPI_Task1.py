cocktail_recipes = {}

with open('cocktails.txt', 'r', encoding='utf-8') as f:
    for line in f:
        recipe_name = line.strip()
        if not recipe_name:  
            continue
                    
        count = int(next(f).strip())
        
        ingredients = []
        
        for _ in range(count):
            ing_line = next(f).strip()
            name, qty, measure = [part.strip() for part in ing_line.split('|')]
            
            ingredients.append({'ingredient_name': name, 'quantity': float(qty), 'measure': measure})
            
        cocktail_recipes[recipe_name] = ingredients

# === Тест для Задания №1 ===

print(f"Маргарита:")
for ing in cocktail_recipes['Маргарита']:
    print(f"  - {ing['ingredient_name']}: {ing['quantity']} {ing['measure']}")