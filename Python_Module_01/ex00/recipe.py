#!/usr/bin/env python3

class Recipe:
    """
        Class that represents a recipe.
            name: str
            cooking_lvl: int
            cooking_time: int
            ingredients: list[str]
            description: str
            recipe_type: str (starter, lunch, dessert)
    """

    def __init__(self,
                 name: str,
                 cooking_lvl: int,
                 cooking_time: int,
                 ingredients: list[str],
                 description: str,
                 recipe_type: str):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(cooking_lvl, int):
            raise TypeError("cooking_lvl must be an integer")
        if not isinstance(cooking_time, int):
            raise TypeError("cooking_time must be an integer")
        if not isinstance(ingredients, list):
            raise TypeError("ingredients must be a list")
        if any(not isinstance(ingredient, str) for ingredient in ingredients):
            raise TypeError("ingredients must be a list of strings")
        if not isinstance(description, str):
            raise TypeError("description must be a string")
        if not isinstance(recipe_type, str):
            raise TypeError("recipe_type must be a string")
        if not name:
            raise ValueError("name must not be empty")
        if cooking_lvl < 1 or cooking_lvl > 5:
            raise ValueError("cooking_lvl must be between 1 and 5")
        if cooking_time < 0:
            raise ValueError("cooking_time must be positive")
        if recipe_type not in ["starter", "lunch", "dessert"]:
            raise ValueError("recipe_type must be starter, lunch or dessert")
        if not ingredients:
            raise ValueError("ingredients must not be empty")
        # description can be empty
        if not recipe_type:
            raise ValueError("recipe_type must not be empty")
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        return (f"Recipe {self.name}:\n"
                + f"\tDescription:   {self.description}\n"
                + f"\tCooking level: {self.cooking_lvl}/5\n"
                + f"\tCooking time:  {self.cooking_time} minutes\n"
                + f"\tIngredients:   {self.ingredients}\n"
                + f"\tRecipe type:   {self.recipe_type}\n")


if __name__ == "__main__":
    print(f"{__file__} only contain the class Recipe:\n{Recipe.__doc__}")
