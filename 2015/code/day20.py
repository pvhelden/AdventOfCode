from math import sqrt

from tqdm import tqdm


def find_divisors(number: int, houses: int = 0):
    divisors = set()
    for i in range(1, int(sqrt(number)) + 1):
        if number % i == 0:
            if not houses > 0 or i * houses >= number:
                divisors.add(i)
            if not houses > 0 or number // i * houses >= number:
                divisors.add(number // i)
    return divisors


def find_lowest_house_number(target: int, factor: int = 10, houses: int = 0):
    current = 1
    with tqdm() as pbar:
        while sum(find_divisors(current, houses)) * factor < target:
            current += 1
            pbar.update()
    return current


def main(filename: str) -> tuple:
    with open(filename) as file:
        target = int(file.read())
        return find_lowest_house_number(target), find_lowest_house_number(target, 11, 50)
