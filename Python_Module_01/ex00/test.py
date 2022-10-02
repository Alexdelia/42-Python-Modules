#!/usr/bin/env python3

import sys
from typing import Any

from book import Book
from recipe import Recipe

if __name__ != "__main__":
    sys.exit()

def test(name: str, T: Any):
    """Test"""
    print(f"\033[1;36m>>> {name}\033[0m")
    try:
        print(T)
    except Exception as e:
        print(e)

test("book basic", Book("My book"))
test("None in book name", Book(None))
test("empty book name", Book(""))
test("int in book name", Book(42))


print("None in book name:")
try:
    book = Book(None)
except Exception as e:
    print(e)
print("Empty book name:")
try:
    book = Book("")
except Exception as e:
    print(e)
print("Book name:")
try:
    book = Book("book")
except Exception as e:
    print(e)

print("None in recipe name:")
try:
    recipe = Recipe(None, 1, 1, [""], "a", "lunch")
    print(recipe)
except Exception as e:
    print(e)
print("Empty recipe name:")
try:
    recipe = Recipe("", 1, 1, ["a"], "a", "lunch")
    print(recipe)
except Exception as e:
    print(e)
print("Recipe name:")
try:
    recipe = Recipe("foo", 1, 1, ["a"], "a", "lunch")
    print(recipe)
except Exception as e:
    print(e)
print("None in recipe cooking level:")
try:
    recipe = Recipe("foo", None, 1, ["a"], "a", "lunch")
    print(recipe)
except Exception as e:
    print(e)
print("Recipe cooking level:")
try:
    recipe = Recipe("foo", 1, 1, ["a"], "a", "lunch")
    print(recipe)
except Exception as e:
    print(e)
print("None in recipe cooking time:")
try:
    recipe = Recipe("foo", 1, None, ["a"], "a", "lunch")
    print(recipe)
except Exception as e:
    print(e)
