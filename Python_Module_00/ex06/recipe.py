#!/usr/bin/env python3

cookbook = {
    "sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}


def print_recipe(name: str):
    """print a recipe for the given name"""
    if name not in cookbook:
        print("Recipe not found")
        return
    print(f"Recipe for {name}:")
    print(f"\tIngredients list: {cookbook[name]['ingredients']}")
    print(f"\tTo be eaten for {cookbook[name]['meal']}.")
    print(f"\tTakes {cookbook[name]['prep_time']} minutes of cooking.\n")


def delete_recipe(name: str):
    """delete a recipe for the given name"""
    if name not in cookbook:
        print("Recipe not found")
        return
    del cookbook[name]


def add_recipe(name: str, ingredients: 'list[str]', meal: str, prep_time: int):
    """add a recipe for the given name"""
    cookbook[name] = {
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time
    }


def add_recipe_interactive():
    """add a recipe interactively"""
    name = input("Recipe name\n>> ")
    while name in cookbook:
        print("Recipe already exists")
        name = input("Recipe name:\n>> ")
    # ingredients = sys.stdin.readlines()
    ingredients: 'list[str]' = []
    i = input("Ingredient:\n>> ")
    while i != "":
        ingredients.append(i)
        i = input("Ingredient:\n>> ")
    meal = input("Meal:\n>> ")
    prep_time = 0
    b = True
    while b:
        try:
            prep_time = int(input("Preparation time:\n>> "))
            b = False
        except ValueError:
            print("Please enter a number")
    add_recipe(name, ingredients, meal, prep_time)


def print_cookbook():
    """print all recipes"""
    for name in cookbook:
        print_recipe(name)


def print_menu():
    """print the menu"""
    print("List of available options:")
    print("\t1: Add a recipe")
    print("\t2: Delete a recipe")
    print("\t3: Print a recipe")
    print("\t4: Print the cookbook")
    print("\t5: Quit\n")


if __name__ == "__main__":
    print("Welcome to the Python Cookbook !")
    print_menu()

    o = 0
    while o != 5:
        try:
            o = int(input("Please select an option:\n>> "))
        except ValueError:
            print("Sorry, this option does not exist.")
            print_menu()
            continue
        print()
        if o == 1:
            add_recipe_interactive()
        elif o == 2:
            delete_recipe(input("Recipe name:\n>> "))
        elif o == 3:
            print_recipe(input("Recipe name:\n>> "))
        elif o == 4:
            print_cookbook()
        elif o == 5:
            print("Cookbook closed. Goodbye !")
        else:
            print("Sorry, this option does not exist.")
            print_menu()
