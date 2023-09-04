from itertools import permutations

from tqdm import tqdm


def parse_happiness_data(lines: list[str]):
    relations: dict[int, dict[int, int]] = dict()
    persons: dict[str, int] = dict()

    for line in lines:
        parts = line.strip('.').split()
        person1 = parts[0]
        person2 = parts[-1]

        persons.setdefault(person1, len(persons))
        persons.setdefault(person2, len(persons))
        relations.setdefault(persons[person1], dict())

        happiness = int(parts[3]) * (-1 if parts[2] == 'lose' else 1)
        relations[persons[person1]][persons[person2]] = happiness

    return relations


def get_max_remaining(persons: list[int], highests: list[int]):
    return sum([highests[person] for person in persons])


def find_max_happiness(input_list: list[str]):
    relations = parse_happiness_data(input_list)
    highests = [sum(sorted(relations[person].values())[-2:]) for person in sorted(relations)]
    max_happiness = 0
    with tqdm() as pbar:
        for perm in permutations(range(1, len(relations))):
            perm = [0] + [*perm]
            happiness = 0

            for index, person in enumerate(perm):
                pbar.update()
                if happiness + get_max_remaining(perm[index:], highests) < max_happiness:
                    break
                left = perm[index - 1]
                right = perm[index + 1 if index + 1 < len(perm) else 0]
                happiness += relations[person][left]
                happiness += relations[person][right]

            if happiness > max_happiness:
                max_happiness = happiness

        pbar.update()

    return max_happiness


def main(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()
        return find_max_happiness(lines), None
