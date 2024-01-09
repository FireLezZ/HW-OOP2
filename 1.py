def read_recipe_file(file_path):
    recipes = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        i = 0
        while i < len(lines):
            # Пропускаем пустые строки
            while i < len(lines) and not lines[i].strip():
                i += 1

            # Проверка, достигли ли конца файла
            if i == len(lines):
                break

            # Чтение названия блюда
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

print(cook_book)
