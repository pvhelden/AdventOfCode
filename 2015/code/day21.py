import re
from itertools import product, combinations

weapons = ((8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0))
armours = ((0, 0, 0), (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5))
rings = ((0, 0, 0), (0, 0, 0), (25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3))
inventory_combinations = tuple(tuple(comb) for comb in product(weapons, armours, combinations(rings, 2)))
player_base = (100, 0, 0)


def parse_character(lines: str) -> list[int]:
    return [int(stat) for stat in re.findall(r'(\d+)', lines)]


def fight(player: list[int], enemy: list[int]) -> bool:
    while player[0] > 0 and enemy[0] > 0:
        enemy[0] -= max(1, player[1] - enemy[2])
        player[0] -= max(1, enemy[1] - player[2])

    return enemy[0] <= 0


def add_to_player(player: list[int], inventory: tuple) -> int:
    cost = 0
    flat_inventory = list(inventory[:2])
    flat_inventory.extend(inventory[2])
    for item in flat_inventory:
        player[1] += item[1]
        player[2] += item[2]
        cost += item[0]
    return cost


def get_lowest_winning_cost(enemy: list[int]) -> int:
    best = float('inf')

    for inventory in inventory_combinations:
        player = list(player_base)
        cost = add_to_player(player, inventory)

        if fight(player, enemy.copy()):
            best = min(best, cost)

    return best


def get_highest_losing_cost(enemy: list[int]) -> int:
    worst = 0

    for inventory in inventory_combinations:
        player = list(player_base)
        cost = add_to_player(player, inventory)

        if not fight(player, enemy.copy()):
            worst = max(worst, cost)

    return worst


def main(filename: str) -> tuple[int, int]:
    with open(filename) as file:
        lines = file.read()
        enemy = parse_character(lines)
        return get_lowest_winning_cost(enemy), get_highest_losing_cost(enemy)
