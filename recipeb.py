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

start()