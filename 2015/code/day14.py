import re


def find_total_distance(speed: int, endurance: int, rest: int, time: int):
    cycle = endurance + rest
    n_cycles = time // cycle
    extra_time = min(time % cycle, endurance)
    return speed * (endurance * n_cycles + extra_time)


def find_best_distance(reindeers: [str], time=2503):
    best = 0
    for reindeer in reindeers:
        values = [int(value) for value in re.findall(r'\d+', reindeer)]
        distance = find_total_distance(*values, time)
        if distance > best:
            best = distance
    return best


def main(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()
        return find_best_distance(lines), 0
