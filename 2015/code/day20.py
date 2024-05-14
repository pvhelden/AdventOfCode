from math import sqrt

from tqdm import tqdm


def find_divisors(number: int):
    divisors = set()
    for i in range(1, int(sqrt(number)) + 1):
        if number % i == 0:
            divisors.add(i)
            divisors.add(number // i)
    return divisors


def find_lowest_house_number(target: int):
    current = 1
    with tqdm() as pbar:
        while sum(find_divisors(current)) * 10 < target:
            current += 1
            pbar.update()
    return current


def main(filename: str) -> tuple:
    with open(filename) as file:
        target = int(file.read())
        return find_lowest_house_number(target), None
