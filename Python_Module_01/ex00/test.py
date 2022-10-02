#!/usr/bin/env python3

import sys
from typing import Any

from book import Book
from recipe import Recipe

if __name__ != "__main__":
    sys.exit()

g = 0
b = 0

def test(name: str, ev: str):
    """Test"""
    print(f"\033[1;36m>>> {name}\033[0m")
    print(f"$\033[1;33m{ev}\033[0m")
    try:
        ret = eval(ev)
        print(f"{ret}%*s" % (42 - len(str(ret)), "\033[1m[\033[31m✗\033[0m\033[1m]"))
    except Exception as e:
        print(e, f"%*s" % (42 - len(str(e)), "\033[1m[\033[31m✗\033[0m\033[1m]"))
        global b
        b+=1
    else:
        global g
        g+=1

test("book basic", 'Book("My book")')
test("None in book name", 'Book(None)')
test("empty book name", 'Book("")')
test("int in book name", 'Book(42)')
test("None in recipe name", 'Recipe(None, 1, 1, ["a", "b"], "desc", "lunch")')
test("empty recipe name", 'Recipe("", 1, 1, ["a", "b"], "desc", "lunch")')
test("int in recipe name", 'Recipe(42, 1, 1, ["a", "b"], "desc", "lunch")')
test("None in recipe cooking level", 'Recipe("name", None, 1, ["a", "b"], "desc", "lunch")')
test("invalid recipe cooking level", 'Recipe("name", 42, 1, ["a", "b"], "desc", "lunch")')
test("None in recipe cooking time", 'Recipe("name", 1, None, ["a", "b"], "desc", "lunch")')
test("invalid recipe cooking time", 'Recipe("name", 1, -42, ["a", "b"], "desc", "lunch")')
test("None in recipe ingredients", 'Recipe("name", 1, 1, None, "desc", "lunch")')
test("int in recipe ingredients", 'Recipe("name", 1, 1, 42, "desc", "lunch")')
test("empty recipe ingredients", 'Recipe("name", 1, 1, [], "desc", "lunch")')
test("None in recipe description", 'Recipe("name", 1, 1, ["a", "b"], None, "lunch")')
test("int in recipe description", 'Recipe("name", 1, 1, ["a", "b"], 42, "lunch")')
test("empty recipe description", 'Recipe("name", 1, 1, ["a", "b"], "", "lunch")')
test("None in recipe recipe_type", 'Recipe("name", 1, 1, ["a", "b"], "desc", None)')
test("int in recipe recipe_type", 'Recipe("name", 1, 1, ["a", "b"], "desc", 42)')
test("empty recipe recipe_type", 'Recipe("name", 1, 1, ["a", "b"], "desc", "")')
test("invalid recipe recipe_type", 'Recipe("name", 1, 1, ["a", "b"], "desc", "invalid")')



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

print(f"\n\t[ \033[1;32m{g}\033[0m|\033[1;31m{b}\033[0m / \033[1m{g+b}\033[0m ]",
      f"\t\033[1;36m{g/(g+b)*100:.2f}%\033[0m",
      "\t\033[1m[",
      ["\033[31mKO", "\033[32mOK"][b == 0],
      "\033[0m\033[1m]")
