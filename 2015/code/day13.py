from itertools import permutations

from tqdm import tqdm


def parse_happiness_data(lines: list[str]):
    happiness_data = {}

    for line in lines:
        parts = line.strip('.').split()
        person1 = parts[0]
        person2 = parts[-1]
        happiness = int(parts[3]) * (-1 if parts[2] == 'lose' else 1)

        happiness_data.setdefault(person1, dict())
        happiness_data[person1][person2] = happiness

    return happiness_data


def find_max_happiness(input_list: list[str]):
    happiness_data = parse_happiness_data(input_list)
    max_happiness = 0
    for perm in tqdm(permutations(happiness_data.keys())):
        happiness = 0

        for person1, person2 in zip(perm, perm[1:] + tuple([perm[0]])):
            happiness += happiness_data[person1][person2]
            happiness += happiness_data[person2][person1]

        if happiness > max_happiness:
            max_happiness = happiness

    return max_happiness


def main(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()
        return find_max_happiness(lines), None
