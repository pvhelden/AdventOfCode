import re


def get_numbers(reindeers: [str]):
    stats = []
    for reindeer in reindeers:
        stats.append([int(value) for value in re.findall(r'\d+', reindeer)])
    return stats


def find_total_distance(speed: int, endurance: int, rest: int, time: int):
    cycle = endurance + rest
    n_cycles = time // cycle
    extra_time = min(time % cycle, endurance)
    return speed * (endurance * n_cycles + extra_time)


def find_best_distance(stats: [int], time=2503):
    best = 0
    index = -1
    for i, reindeer in enumerate(stats):
        distance = find_total_distance(*reindeer, time=time)
        if distance > best:
            best = distance
            index = i
    return best, index


def find_best_score(stats: [int], time=2503):
    scores = [0] * len(stats)
    for current in range(time):
        _, index = find_best_distance(stats, time=current)
        scores[index] += 1
    return max(scores)


def race_distance(lines: [str], time=2503):
    stats = get_numbers(lines)
    return find_best_distance(stats, time)[0]


def race_score(lines: [str], time=2503):
    stats = get_numbers(lines)
    return find_best_score(stats, time)


def main(filename: str):
    with open(filename) as file:
        lines = file.read().splitlines()
        return race_distance(lines), race_score(lines)
