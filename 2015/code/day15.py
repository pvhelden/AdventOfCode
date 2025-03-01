import itertools
import re

import numpy as np


def get_props(ingredient: str):
    return [int(match) for match in re.findall(r'-?\d+', ingredient)]


def find_combinations(total, num_variables):
    possible_permutations = []

    # Generate all possible permutations of teaspoons for the given number of ingredients
    for permutation in itertools.product(range(total + 1), repeat=num_variables):
        if sum(permutation) == total:
            possible_permutations.append(permutation)

    return possible_permutations


def objective_function(quantities, properties):
    scores = []
    for y in range(len(properties[0])):
        score = []
        for x in range(len(quantities)):
            score.append(quantities[x] * properties[x][y])
        total = sum(score)
        if total < 0:
            return 0, 0
        scores.append(total)
    return np.prod(scores[:-1]), scores[-1]


def solve_function(ingredients: list[str], calorie_count=0):
    properties = [get_props(ingredient) for ingredient in ingredients]
    shitte = find_combinations(100, len(properties))
    best_score = 0
    for combination in shitte:
        score, calories = objective_function(combination, properties)
        if (calorie_count and calories == calorie_count) or not calorie_count:
            if score > best_score:
                best_score = score
    return best_score


def main(filename: str) -> tuple:
    with open(filename) as file:
        lines = file.read().splitlines()
        return solve_function(lines), solve_function(lines, 500)
