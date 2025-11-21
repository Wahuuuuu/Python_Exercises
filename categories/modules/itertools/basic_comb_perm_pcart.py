"""
This code is to solve a series of basic, little questions
related to the members of the itertool module.
"""
from itertools import combinations
from itertools import permutations
from itertools import product

"""
P1: Coffee bar
---
The boss of a coffee bar has work for us...
Using these lists below, we have to create: 
    1. every combinations of a pair of drinks
    2. every order of the toppings
    3. a list of menu with format: size x drink x topping
    sizes = ["S", "M"]
    drinks = ["latte", "mocha", "tea"]
    toppings = ["pearls", "cream"]
"""
def solve_coffee_bar() -> None:
    sizes: list[str] = ["S", "M"]
    drinks: list[str] = ["latte", "mocha", "tea"]
    toppings: list[str] = ["pearls", "cream"]

    print("Combinations of a pair of drink:")
    for pair in combinations(drinks, 2):
        print(pair)
    print()

    print("Order of the toppings:")
    for order in permutations(toppings, 2):
        print (order)
    print()

    print("Menu: ")
    for size, drink, topping in product(sizes, drinks, toppings):
        print(f"{size} x {drink} x {topping}")


solve_coffee_bar()
