import re


def get_numbers(reindeers: list[str]) -> list[list[int]]:
    """
    Extracts numbers from strings representing reindeer stats.

    Args:
    - reindeers (list of str): List of strings representing reindeer stats.

    Returns:
    - list: List of lists, where each inner list contains integers extracted from the corresponding reindeer stat string.
    """
    stats = []
    for reindeer in reindeers:
        stats.append([int(value) for value in re.findall(r'\d+', reindeer)])
    return stats


def find_total_distance(speed: int, endurance: int, rest: int, time: int) -> int:
    """
    Calculates the total distance traveled by a reindeer over a given time.

    Args:
    - speed (int): Speed of the reindeer.
    - endurance (int): Duration of the reindeer's flight period.
    - rest (int): Duration of the reindeer's rest period.
    - time (int): Total time for which the distance needs to be calculated.

    Returns:
    - int: Total distance traveled by the reindeer.
    """
    cycle = endurance + rest
    n_cycles = time // cycle
    extra_time = min(time % cycle, endurance)
    return speed * (endurance * n_cycles + extra_time)


def find_best_distance(stats: list[list[int]], time=2503) -> tuple[int, int]:
    """
    Finds the distance traveled by the reindeer that has traveled the farthest.

    Args:
    - stats (list of int): List of lists containing the stats of each reindeer.
    - time (int, optional): Total time for which the distance needs to be calculated. Defaults to 2503.

    Returns:
    - tuple: A tuple containing the distance traveled by the best reindeer and its index in the stats list.
    """
    best = 0
    index = -1
    for i, reindeer in enumerate(stats):
        distance = find_total_distance(*reindeer, time=time)
        if distance > best:
            best = distance
            index = i
    return best, index


def find_best_score(stats: list[list[int]], time=2503) -> int:
    """
    Finds the maximum score obtained by any reindeer over the given time.

    Args:
    - stats (list of int): List of lists containing the stats of each reindeer.
    - time (int, optional): Total time for which the scores need to be calculated. Defaults to 2503.

    Returns:
    - int: The maximum score obtained by any reindeer.
    """
    scores = [0] * len(stats)
    for current in range(time):
        _, index = find_best_distance(stats, time=current)
        scores[index] += 1
    return max(scores)


def race_distance(lines: list[str], time=2503) -> int:
    """
    Simulates a race to find the distance traveled by the winning reindeer.

    Args:
    - lines (list of str): List of strings representing the stats of each reindeer.
    - time (int, optional): Total time for which the race needs to be simulated. Defaults to 2503.

    Returns:
    - int: The distance traveled by the winning reindeer.
    """
    stats = get_numbers(lines)
    return find_best_distance(stats, time)[0]


def race_score(lines: list[str], time=2503) -> int:
    """
    Simulates a race to find the maximum score obtained by any reindeer.

    Args:
    - lines (list of str): List of strings representing the stats of each reindeer.
    - time (int, optional): Total time for which the race needs to be simulated. Defaults to 2503.

    Returns:
    - int: The maximum score obtained by any reindeer.
    """
    stats = get_numbers(lines)
    return find_best_score(stats, time)


def main(filename: str) -> tuple:
    with open(filename) as file:
        lines = file.read().splitlines()
        return race_distance(lines), race_score(lines)
