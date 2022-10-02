#!/usr/bin/env python3

import sys
from typing import Any
from xmlrpc.client import FastParser

from book import Book
from recipe import Recipe

if __name__ != "__main__":
    sys.exit()

g = 0
b = 0

def handle_res(out: str, success: bool):
    """
        Print the result of a test and update global variables
            out: str      (output of the test)
            success: bool (if the test was successful)
    """
    l = 80 - len(out)
    l = [l, 0][l < 0]
    print(f"{out}%*s" % (l, "\033[1m["), end="")
    if success:
        print("\033[32m✔\033[0m\033[1m]")
        global g
        g+=1
    else:
        print("\033[31m✗\033[0m\033[1m]")
        global b
        b+=1

def test(name: str, ev: str, b_ex: bool = True) -> None:
    """
        Test:
            name: str         (name of the test)
            ev: str           (evaluated string)
            b_ex: bool = True (expected result)
    """
    print(f"\033[1;36m>>> {name}\033[0m")
    print(f"$\033[1;33m{ev}\033[0m")
    try:
        handle_res(str(eval(ev)), b_ex)
    except Exception as e:
        handle_res(str(e), not b_ex)

test("book basic", 'Book("My book")', True)
test("None in book name", 'Book(None)', False)
test("empty book name", 'Book("")', False)
test("int in book name", 'Book(42)', False)
test("recipe basic", 'Recipe("My recipe", 1, 10, ["a", "b", "c"], "desc", "lunch")', True)
test("recipe basic print", 'str(Recipe("sandwhich", 1, 4, ["bread", "ham", "cheese", "butter"], "a nice butter/ham/sandwhich", "lunch"))', True)
test("None in recipe name", 'Recipe(None, 1, 1, ["a", "b"], "desc", "lunch")', False)
test("empty recipe name", 'Recipe("", 1, 1, ["a", "b"], "desc", "lunch")', False)
test("int in recipe name", 'Recipe(42, 1, 1, ["a", "b"], "desc", "lunch")', False)
test("None in recipe cooking level", 'Recipe("name", None, 1, ["a", "b"], "desc", "lunch")', False)
test("invalid recipe cooking level", 'Recipe("name", 42, 1, ["a", "b"], "desc", "lunch")', False)
test("None in recipe cooking time", 'Recipe("name", 1, None, ["a", "b"], "desc", "lunch")', False)
test("invalid recipe cooking time", 'Recipe("name", 1, -42, ["a", "b"], "desc", "lunch")', False)
test("None in recipe ingredients", 'Recipe("name", 1, 1, None, "desc", "lunch")', False)
test("int in recipe ingredients", 'Recipe("name", 1, 1, 42, "desc", "lunch")', False)
test("empty recipe ingredients", 'Recipe("name", 1, 1, [], "desc", "lunch")', False)
test("None in recipe description", 'Recipe("name", 1, 1, ["a", "b"], None, "lunch")', False)
test("int in recipe description", 'Recipe("name", 1, 1, ["a", "b"], 42, "lunch")', False)
# empty recipe description is valid
test("empty recipe description", 'Recipe("name", 1, 1, ["a", "b"], "", "lunch")', True)
test("None in recipe recipe_type", 'Recipe("name", 1, 1, ["a", "b"], "desc", None)', False)
test("int in recipe recipe_type", 'Recipe("name", 1, 1, ["a", "b"], "desc", 42)', False)
test("empty recipe recipe_type", 'Recipe("name", 1, 1, ["a", "b"], "desc", "")', False)
test("invalid recipe recipe_type", 'Recipe("name", 1, 1, ["a", "b"], "desc", "invalid")', False)
test("book add recipe", 'str(b = Book("My book"); b.add_recipe(Recipe("My recipe", 1, 10, ["a", "b", "c"], "desc", "lunch")); b.get_recipe_by_name("My recipe"))', True)
test("book add and get recipe", 'b = Book("My book"); b.add_recipe(Recipe("My recipe", 1, 10, ["a", "b", "c"], "desc", "lunch")); b.get_recipe_by_name("My recipe")', True)
test("book get unadd recipe", 'b = Book("My book"); b.get_recipe_by_name("My recipe")', False)
test("test", 'book = Book("My book") and book.add_recipe(Recipe("My recipe", 1, 10, ["a", "b", "c"], "desc", "lunch")) and book.get_recipe_by_name("My recipe")', True)
