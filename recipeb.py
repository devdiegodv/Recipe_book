import os
from pathlib import Path
from os import system

my_path = Path(Path.home(), "Recipes")
print(my_path)

def count_recipes(path):
    count = 0

    for txt in Path(path).glob("**/*.txt"):
        count += 1
        print(txt)
    return count

def start():
    system('cls')
    print('*' * 50)
    print('*' * 5 + "Welcome to the recipe's administrator")
    print('*' * 50)
    print('\n')
    print(f"The recipes are in {my_path}")
    print(f"Total recipes: {count_recipes(my_path)}")

    menu_select = 'x'
    while not menu_select.isnumeric() or int(menu_select) not in range(1,7):
        print('Choose an option:')
        print('''
            [1] - Read a recipe
            [2] - Make a new recipe
            [3] - Make a new category
            [4] - Delete recipe
            [5] - Delete category
            [6] - Get out''')
        
        menu_select = input()
    return (menu_select)

def show_categories(path):
    print("Categories:")
    categories_path = Path(path)
    categories_list = []
    count = 1

    for folder in categories_path.iterdir():
        folder_str = str(folder.name)
        print(f"[{count}] - {folder_str}")
        categories_list.append(folder)
        count += 1
    
    return categories_list

def choose_category(list):
    correct_select = 'x'

    while not correct_select.isnumeric() or int(correct_select) not in range(1, len(list) + 1):
        correct_select = input('\nChoose a category:')

    return list[int(correct_select) - 1]

def show_recipes(path):
    print('Recipes:')
    path_recipes = Path(path)
    recipes_list = []
    count = 1

    for recipe in path_recipes.glob('*.txt'):
        recipe_str = str(recipe.name)
        print(f"[{count}] - {recipe_str}")
        recipes_list.append(recipe)
        count += 1

    return recipes_list

def choose_recipe(list):
    recipe_select = 'x'

    while not recipe_select.isnumeric() or int(recipe_select) not in range(1, len(list) + 1):
        recipe_select = input('\nChoose a recipe: ')
    
    return list[int(recipe_select) - 1]

menu = 0

if menu == 1:
    my_categories = show_categories(my_path)
    my_category = choose_category(my_categories)
    my_recipes = show_recipes(my_category)
    my_recipe = choose_recipe(my_recipes)
    pass
elif menu == 2:
    my_categories = show_categories(my_path)
    my_category = choose_category(my_categories)
    pass
elif menu == 3:
    pass
elif menu == 4:
    my_categories = show_categories(my_path)
    my_category = choose_category(my_categories)
    my_recipes = show_recipes(my_category)
    my_recipe = choose_recipe(my_recipes)
    pass
elif menu == 5:
    my_categories = show_categories(my_path)
    my_category = choose_category(my_categories)

start()