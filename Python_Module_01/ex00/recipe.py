from enum import Enum

from pydantic import (
    BaseModel, ConstrainedInt, ConstrainedStr, Field, StrictStr
)


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


class RecipeType(str, Enum):
    STARTER = "starter"
    LUNCH = "lunch"
    DESSERT = "dessert"


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
        return f"""\
Recipe {self.name}:
\tDescription:   {self.description}
\tCooking level: {self.cooking_lvl}/5
\tCooking time:  {self.cooking_time} minutes
\tIngredients:   {str(self.ingredients)[1:1]}
\tRecipe type:   {self.recipe_type.value}
"""


if __name__ == "__main__":
    print(f"{__file__} only contain the class Recipe:\n{Recipe.__doc__}")
