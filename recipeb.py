import os
from pathlib import Path
from os import system

my_path = Path(Path.home(), "Recipes")
print(my_path)

def count_recipes(path):
    '''

    count_recipes: Counts and prints the total number of recipes in the specified path.

    '''
    count = 0

    for txt in Path(path).glob("**/*.txt"):
        count += 1
        print(txt)
    return count


def start():
    '''

    start: Displays the main menu and returns the user's menu selection.

    '''
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
    return int(menu_select)

def show_categories(path):
    '''

    show_categories: Lists and prints available categories in the given path.

    '''
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
    '''

    choose_category: Takes user input to choose a category from the list.

    '''
    correct_select = 'x'

    while not correct_select.isnumeric() or int(correct_select) not in range(1, len(list) + 1):
        correct_select = input('\nChoose a category:')

    return list[int(correct_select) - 1]

def show_recipes(path):
    '''

    show_recipes: Lists and prints available recipes in the given path.

    '''
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
    '''

    choose_recipe: Takes user input to choose a recipe from the list.

    '''
    recipe_select = 'x'

    while not recipe_select.isnumeric() or int(recipe_select) not in range(1, len(list) + 1):
        recipe_select = input('\nChoose a recipe: ')
    
    return list[int(recipe_select) - 1]

def read_recipe(recipe):
    '''

    read_recipe: Reads and prints the content of the selected recipe.

    '''
    print(Path.read_text(recipe))


def create_recipe(path):
    '''

    create_recipe: Takes user input to create a new recipe in the specified category.

    '''
    exist = False

    while not exist:
        print("Write your recipe's name: ")
        recipe_name = input() + '.txt'
        print("Write your recipe's description: ")
        recipe_content = input()
        new_path = Path(path, recipe_name)  

        if not os.path.exists(new_path):
            Path.write_text(new_path, recipe_content)
            print(f'Your recipe {recipe_name} has been created')
            exist = True
        else:
            print('I am sorry, that recipe already exists')

def create_category(path):
    '''

    create_category: Takes user input to create a new category.

    '''
    exist = False

    while not exist:
        print('Write the name of your new category: ')
        category_name = input()
        new_path = Path(path, category_name)  

        if not os.path.exists(new_path):
            Path.mkdir(new_path)
            print(f'Your new category {category_name} has been created')
            exist = True
        else:
            print('I am sorry, that category already exists')

def delete_recipe(recipe):
    '''

    delete_recipe: Deletes the specified recipe.

    '''
    Path(recipe).unlink()
    print(f'The recipe {recipe.name} has been deleted')

def delete_category(category):
    '''

    delete_category: Deletes the specified category.

    '''
    Path(category).rmdir()
    print(f'The category {category.name} has been deleted')

def back_to_menu():
    '''

    back_to_menu: Allows the user to return to the main menu by pressing 'V'.

    '''
    back_select = 'x'

    while back_select.lower() != 'v':
        back_select = input('\nPress V to back to the start menu: ')

end_software = False

while not end_software:
    menu = start()

    if menu == 1:
        my_categories = show_categories(my_path)
        my_category = choose_category(my_categories)
        my_recipes = show_recipes(my_category)
        if len(my_recipes) < 1:
            print('No recipes in this category')
        else:
            my_recipe = choose_recipe(my_recipes)
            read_recipe(my_recipe)
        back_to_menu()

    elif menu == 2:
        my_categories = show_categories(my_path)
        my_category = choose_category(my_categories)
        create_recipe(my_category)
        back_to_menu()

    elif menu == 3:
        create_category(my_path)
        back_to_menu()

    elif menu == 4:
        my_categories = show_categories(my_path)
        my_category = choose_category(my_categories)
        my_recipes = show_recipes(my_category)
        if len(my_recipes) < 1:
            print('No recipes in this category')
        else:
            my_recipe = choose_recipe(my_recipes)
            delete_recipe(my_recipe)
        back_to_menu()

    elif menu == 5:
        my_categories = show_categories(my_path)
        my_category = choose_category(my_categories)
        delete_category(my_category)
        back_to_menu()

    elif menu == 6:
        end_software = True

