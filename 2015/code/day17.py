def parse_containers(lines: [str]):
    return sorted([int(container) for container in lines], reverse=True)


def recursive_container(max_volume, used, remaining, combinations):
    if sum(used) == max_volume:
        combinations.append(used.copy())
    elif sum(used) < max_volume:
        for i in range(len(remaining)):
            recursive_container(max_volume, used + [remaining[i]], remaining[i + 1:], combinations)


def fit_containers(lines: [str], max_volume: int):
    containers = parse_containers(lines)
    combinations = []
    recursive_container(max_volume, [], containers, combinations)
    return len(combinations)


def main(filename: str) -> tuple:
    with open(filename) as file:
        lines = file.read().splitlines()
        return fit_containers(lines, 150), None
