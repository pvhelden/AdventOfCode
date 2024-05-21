def parse_containers(lines: list[str]):
    return sorted([int(container) for container in lines], reverse=True)


def recursive_container(max_volume, used, remaining, combinations):
    if sum(used) == max_volume:
        combinations.append(used)
    elif sum(used) < max_volume:
        for i in range(len(remaining)):
            recursive_container(max_volume, used + [remaining[i]], remaining[i + 1:], combinations)


def get_combinations(lines: list[str], max_volume: int):
    containers = parse_containers(lines)
    combinations = []
    recursive_container(max_volume, [], containers, combinations)
    return combinations


def get_number_combinations(lines: list[str], max_volume: int):
    return len(get_combinations(lines, max_volume))


def get_number_shortest_combinations(lines: list[str], max_volume: int):
    combinations = get_combinations(lines, max_volume)
    lengths = [len(combination) for combination in combinations]
    return lengths.count(min(lengths))


def main(filename: str) -> tuple:
    with open(filename) as file:
        lines = file.read().splitlines()
        return get_number_combinations(lines, 150), get_number_shortest_combinations(lines, 150)
