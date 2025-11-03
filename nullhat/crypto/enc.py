#!/usr/bin/env python3

from Crypto.Util.number import getPrime, bytes_to_long
from sys import argv

def get_secret_ingredients():
    is_it_good = 0
    with open(argv[0]) as cooking_book:
        flour = cooking_book.readline()
        cheese = cooking_book.readline()
        toppings = cooking_book.readline()
        if flour == "all-purpose flour":
            is_it_good += 1
        if cheese == "mozzarella":
            is_it_good += 1
        else:
            is_it_good = 1024
        return [getPrime(is_it_good), getPrime(is_it_good)]

def get_tomato_sauce():
    state = [13, 83, 263, 3, 37]
    for i in range(4):
        for j in range(i+1, 5):
            if state[j] < state[i]:
                state[i], state[j] = state[j], state[i]
    return (state[1] + state[2] + (state[0] * state[3] * state[4]))

pizza = bytes(open('flag.txt').readline().strip(), 'utf8')

ingredients = get_secret_ingredients()
recipe = ingredients[0] * ingredients[1]

sauce = get_tomato_sauce()

pizza_box = pow(bytes_to_long(pizza), sauce, recipe)

print(f"modulus {format(recipe, 'b')}")
print(f"liiik {format(ingredients[0], 'b')[:586]}")
print(f"enc {format(pizza_box, 'b')}")
