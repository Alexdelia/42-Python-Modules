#!/usr/bin/env python3

from enum import StrEnum, auto
from typing import Literal

from pydantic import (BaseModel, ConstrainedInt, ConstrainedStr, Field,
                      StrictStr)


class UnEmptyStr(ConstrainedStr):
    strict = True
    min_length = 1


class CookingLvl(ConstrainedInt):
    strict = True
    ge = 1
    le = 5


class PositiveInt(ConstrainedInt):
    strict = True
    ge = 0


class RecipeType(StrEnum):
    STARTER = auto()
    LUNCH = auto()
    DESSERT = auto()


class Recipe(BaseModel):
    """
        Class that represents a recipe.
            name: str
            cooking_lvl: int
            cooking_time: int
            ingredients: list[str]
            description: str
            recipe_type: str (starter, lunch, dessert)
    """
    name: UnEmptyStr
    cooking_lvl: CookingLvl
    cooking_time: PositiveInt
    ingredients: list[UnEmptyStr] = Field(..., min_items=1)
    description: StrictStr
    recipe_type: RecipeType

    def __init__(
        self,
        name: str,
        cooking_lvl: int,
        cooking_time: int,
        ingredients: list[str],
        description: str,
        recipe_type: str,
    ):
        super().__init__(
            name=name,
            cooking_lvl=cooking_lvl,
            cooking_time=cooking_time,
            ingredients=ingredients,
            description=description,
            recipe_type=recipe_type,
        )

    def __str__(self):
        """Return the string to print with the recipe info"""
        return (
            f"Recipe {self.name}:\n" + f"\tDescription:   {self.description}\n"
            + f"\tCooking level: {self.cooking_lvl}/5\n"
            + f"\tCooking time:  {self.cooking_time} minutes\n"
            + f"\tIngredients:   {self.ingredients}\n"
            + f"\tRecipe type:   {self.recipe_type}\n"
        )


if __name__ == "__main__":
    print(f"{__file__} only contain the class Recipe:\n{Recipe.__doc__}")
