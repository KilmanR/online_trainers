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

# Задание 2:

def get_shop_list_by_drinks(drinks, person_count):
    shop_list = {}
    
    for drink in drinks:
        if drink not in cocktail_recipes:
            continue
            
        for ing in cocktail_recipes[drink]:
            name = ing['ingredient_name']
            qty = ing['quantity'] * person_count
            measure = ing['measure']
            
            if name in shop_list:
                shop_list[name]['quantity'] += qty  
            else:
                shop_list[name] = {'measure': measure, 'quantity': qty}
                
    return shop_list

# === Тест для Задания №2 ===

order = ['Мохито', 'Апероль Шприц', 'Мохито']
result = get_shop_list_by_drinks(order, 3)

print("\n Список закупки:")
for name, data in result.items():
    print(f"  {name}: {data['quantity']} {data['measure']}")