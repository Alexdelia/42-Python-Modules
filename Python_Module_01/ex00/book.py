#!/usr/bin/env python3

from datetime import datetime

from pydantic import BaseModel
from recipe import Recipe, UnEmptyStr


class RecipeList(BaseModel):
    starter: list[Recipe]
    lunch: list[Recipe]
    dessert: list[Recipe]


class Book(BaseModel):
    """
        Class that represents a book.
            name: str
            last_update: datetime
            creation_date: datetime
            recipes_list: dict[str, list[Recipe]]
                (str == "starter" or "lunch" or "dessert")

        Methods:
            get_recipe_by_name(name: str): Recipe
            get_recipes_by_types(recipe_type: str): Union[list[Recipe], None]
            add_recipe(recipe: Recipe)
    """

    name: UnEmptyStr
    last_update: datetime
    creation_date: datetime
    recipes_list: dict[str, list[Recipe]]

    def __init__(self, name: str):
        super().__init__(
            name=name,
            last_update=datetime.now(),
            creation_date=datetime.now(),
            recipes_list={
                "starter": [],
                "lunch": [],
                "dessert": [],
            },
        )

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not name:
            raise ValueError("name must not be empty")
        ret = list(
            filter(
                lambda recipe: recipe.name == name, self.recipes_list["lunch"]
                + self.recipes_list["starter"] + self.recipes_list["dessert"]
            )
        )
        ret = ret[0] if ret else None
        print(ret)
        return ret

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if not isinstance(recipe_type, str):
            raise TypeError("recipe_type must be a string")
        if not recipe_type:
            raise ValueError("recipe_type must not be empty")
        if recipe_type not in ["starter", "lunch", "dessert"]:
            raise ValueError("recipe_type must be starter, lunch or dessert")
        return self.recipes_list[recipe_type]

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            raise TypeError("recipe must be a Recipe")
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()


if __name__ == "__main__":
    print(f"{__file__} only contain the class Book:\n{Book.__doc__}")
