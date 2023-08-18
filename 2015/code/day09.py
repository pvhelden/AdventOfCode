from itertools import permutations

from tqdm import tqdm


def build_distance_matrix(distance_strings: list[str]):
    cities = set()
    distances_dict = {}

    for distance_string in tqdm(distance_strings):
        parts = distance_string.split()
        city_from, city_to, distance = parts[0], parts[2], int(parts[4])

        cities.add(city_from)
        cities.add(city_to)

        distances_dict[(city_from, city_to)] = distance
        distances_dict[(city_to, city_from)] = distance

    cities = sorted(cities)
    n = len(cities)
    distances_matrix = [[0] * n for _ in range(n)]

    for i, city_from in tqdm(enumerate(cities)):
        for j, city_to in enumerate(cities):
            if i != j:
                distance = distances_dict.get((city_from, city_to), float('inf'))
                distances_matrix[i][j] = distance
                distances_matrix[j][i] = distance

    return distances_matrix


def day09(distance_strings: list[str]):
    distances_matrix = build_distance_matrix(distance_strings)
    min_distance = float('inf')
    max_distance = 0

    for order in tqdm(permutations(range(len(distances_matrix)))):
        order: tuple[int]  # Type hint, not functional
        distance = 0
        for city_from, city_to in zip(order, order[1:]):
            distance += distances_matrix[city_from][city_to]
        if distance < min_distance:
            min_distance = distance
        if distance > max_distance:
            max_distance = distance
    return min_distance, max_distance


def main(filename: str):
    with open(filename) as file:
        return day09(file.read().splitlines())
