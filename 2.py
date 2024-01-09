def read_recipe_file(file_path):
    recipes = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        i = 0
        while i < len(lines):
            # Пропускаем пустые строки
            while i < len(lines) and not lines[i].strip():
                i += 1
            if i == len(lines):
                break

            # Чтение названия блюд
            dish_name = lines[i].strip()
            i += 1

            # Проверка наличия названия блюда
            if not dish_name:
                print("Ошибка в файле: Название блюда отсутствует.")
                return None

            # Чтение количества ингредиентов в блюде
            try:
                num_ingredients = int(lines[i])
            except ValueError:
                print(f"Ошибка в файле: Неверное количество ингредиентов для блюда '{dish_name}'")
                return None

            i += 1

            # Чтение ингредиентов
            ingredients = []
            for j in range(num_ingredients):
                try:
                    ingredient_info = lines[i].strip().split('|')
                    ingredient_name = ingredient_info[0].strip()
                    quantity = int(ingredient_info[1].strip())
                    measure = ingredient_info[2].strip()
                except (ValueError, IndexError):
                    print(f"Ошибка в файле: Неверный формат ингредиента для блюда '{dish_name}'")
                    return None

                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure  
                })

                i += 1

            # Добавление рецепта в словарь
            recipes[dish_name] = ingredients

    return recipes

file_path = 'recipes.txt'
cook_book = read_recipe_file(file_path)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish_name in dishes:
        if dish_name not in cook_book:
            print(f"Блюдо '{dish_name}' отсутствует в книге рецептов.")
            continue

        ingredients = cook_book[dish_name]
        for ingredient in ingredients:
            ingredient_name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']

            if ingredient_name not in shop_list:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
            else:
                shop_list[ingredient_name]['quantity'] += quantity

    return shop_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))