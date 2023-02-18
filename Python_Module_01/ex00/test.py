from typing import Any

import pytest
from book import Book
from recipe import Recipe, RecipeType

BOOK_NAME = "My book"
RECIPE_NAME = "My recipe"


@pytest.fixture(scope="function")
def recipe_dict() -> dict[str, Any]:
    return {
        "name": RECIPE_NAME,
        "cooking_lvl": 1,
        "cooking_time": 10,
        "ingredients": ["a", "b", "c"],
        "description": "desc",
        "recipe_type": "lunch",
    }


def test_book_basic():
    book = Book(BOOK_NAME)
    assert book.name == BOOK_NAME
    assert book.last_update == book.creation_date
    assert book.recipes_list == {k.value: [] for k in RecipeType}


def test_book_name_invalid():
    with pytest.raises(Exception):
        Book(None)  # type: ignore

    with pytest.raises(Exception):
        Book("")

    with pytest.raises(Exception):
        Book(42)  # type: ignore


def test_recipe_basic(recipe_dict):
    recipe = Recipe(**recipe_dict)
    assert recipe.dict() == recipe_dict
    assert str(recipe) == (
        f"Recipe name: {recipe_dict['name']}\n"
        f"Cooking level: {recipe_dict['cooking_lvl']}\n"
        f"Cooking time: {recipe_dict['cooking_time']}\n"
        f"Ingredients: {recipe_dict['ingredients']}\n"
        f"Description: {recipe_dict['description']}\n"
        f"Recipe type: {recipe_dict['recipe_type']}\n"
    )


def test_recipe_name_invalid(recipe_dict):
    recipe_dict["name"] = None
    with pytest.raises(ValueError):
        Recipe(**recipe_dict)

    recipe_dict["name"] = ""
    with pytest.raises(ValueError):
        Recipe(**recipe_dict)

    recipe_dict["name"] = 42
    with pytest.raises(TypeError):
        Recipe(**recipe_dict)


def test_to_be_sure(recipe_dict):
    assert recipe_dict["name"] == RECIPE_NAME


def test_recipe_cooking_level_invalid(recipe_dict):
    recipe_dict["cooking_lvl"] = None
    with pytest.raises(ValueError):
        Recipe(**recipe_dict)

    recipe_dict["cooking_lvl"] = 42
    with pytest.raises(ValueError):
        Recipe(**recipe_dict)

    recipe_dict["cooking_lvl"] = -42
    with pytest.raises(TypeError):
        Recipe(**recipe_dict)

    recipe_dict["cooking_lvl"] = 1.5
    with pytest.raises(TypeError):
        Recipe(**recipe_dict)

    recipe_dict["cooking_lvl"] = "1"
    with pytest.raises(TypeError):
        Recipe(**recipe_dict)

    recipe_dict["cooking_lvl"] = True
    with pytest.raises(TypeError):
        Recipe(**recipe_dict)

    recipe_dict["cooking_lvl"] = 0
    with pytest.raises(ValueError):
        Recipe(**recipe_dict)


def test_recipe_cooking_time_invalid(recipe_dict):
    recipe_dict["cooking_time"] = None
    with pytest.raises(ValueError):
        Recipe(**recipe_dict)

    recipe_dict["cooking_time"] = -42
    with pytest.raises(ValueError):
        Recipe(**recipe_dict)

    recipe_dict["cooking_time"] = 42.5
    with pytest.raises(TypeError):
        Recipe(**recipe_dict)

    recipe_dict["cooking_time"] = "42"
    with pytest.raises(TypeError):
        Recipe(**recipe_dict)

    recipe_dict["cooking_time"] = True
    with pytest.raises(TypeError):
        Recipe(**recipe_dict)

    recipe_dict["cooking_time"] = 0
    with pytest.raises(ValueError):
        Recipe(**recipe_dict)


def test_recipe_ingredients_invalid(recipe_dict):
    recipe_dict["ingredients"] = None
    with pytest.raises(ValueError):
        Recipe(**recipe_dict)

    recipe_dict["ingredients"] = 42
    with pytest.raises(TypeError):
        Recipe(**recipe_dict)

    recipe_dict["ingredients"] = []
    with pytest.raises(ValueError):
        Recipe(**recipe_dict)

    recipe_dict["ingredients"] = ["a", "", "b"]
    with pytest.raises(ValueError):
        Recipe(**recipe_dict)


def test_recipe_description_invalid(recipe_dict):
    recipe_dict["description"] = None
    with pytest.raises(ValueError):
        Recipe(**recipe_dict)

    recipe_dict["description"] = 42
    with pytest.raises(TypeError):
        Recipe(**recipe_dict)

    # description is the only field that can be empty
    recipe_dict["description"] = ""
    Recipe(**recipe_dict)


def test_recipe_recipe_type_invalid(recipe_dict):
    recipe_dict["recipe_type"] = None
    with pytest.raises(ValueError):
        Recipe(**recipe_dict)

    recipe_dict["recipe_type"] = ""
    with pytest.raises(ValueError):
        Recipe(**recipe_dict)

    recipe_dict["recipe_type"] = 42
    with pytest.raises(TypeError):
        Recipe(**recipe_dict)

    recipe_dict["recipe_type"] = "invalid"
    with pytest.raises(ValueError):
        Recipe(**recipe_dict)

    recipe_dict["recipe_type"] = RecipeType.STARTER.value.upper()
    with pytest.raises(ValueError):
        Recipe(**recipe_dict)


def test_add_recipe(recipe_dict):
    book = Book(BOOK_NAME)

    assert book.recipes_list == {k.value: [] for k in RecipeType}
    assert book.last_update == book.creation_date

    recipe = Recipe(**recipe_dict)

    book.add_recipe(recipe)

    for k in RecipeType:
        if k.value == recipe.recipe_type:
            assert book.recipes_list[k.value] == [recipe]
        else:
            assert book.recipes_list[k.value] == []

    assert book.last_update > book.creation_date


def test_get_recipe_by_name(recipe_dict):
    book = Book(BOOK_NAME)

    assert book.get_recipe_by_name(RECIPE_NAME) is None

    recipe = Recipe(**recipe_dict)

    book.add_recipe(recipe)

    assert book.get_recipe_by_name(RECIPE_NAME) == recipe
    assert book.get_recipe_by_name("invalid") is None


def test_get_recipes_by_types(recipe_dict):
    book = Book(BOOK_NAME)

    assert book.get_recipes_by_types(RecipeType.STARTER.value) == []

    recipe_dict["recipe_type"] = RecipeType.STARTER.value
    recipe = Recipe(**recipe_dict)

    book.add_recipe(recipe)

    assert book.get_recipes_by_types(RecipeType.STARTER.value) == [recipe]
    assert book.get_recipes_by_types(RecipeType.LUNCH.value) == []
    assert book.get_recipes_by_types(RecipeType.DESSERT.value) == []


def test_get_recipes_by_types_invalid(recipe_dict):
    book = Book(BOOK_NAME)

    with pytest.raises(TypeError):
        book.get_recipes_by_types(42)

    with pytest.raises(ValueError):
        book.get_recipes_by_types("")

    with pytest.raises(TypeError):
        book.get_recipes_by_types(None)

    with pytest.raises(ValueError):
        book.get_recipes_by_types("invalid")
