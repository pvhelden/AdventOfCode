from re import findall

from tqdm import tqdm


def find_lengths_diff(string: str):
    # Part 1
    memory = len(string) - 2
    matches = findall(r'\\(?:x\w{2}|\\|\")', string)
    for match in matches:
        memory -= len(match) - 1

    # Part 2
    encoded_diff = len(findall(r'[\\\"]', string)) + 2

    return len(string) - memory, encoded_diff


def compute_sum_lenghts(strings: list[str]):
    memory_diff = 0
    encoded_diff = 0
    for string in tqdm(strings):
        values = find_lengths_diff(string)
        memory_diff += values[0]
        encoded_diff += values[1]
    return memory_diff, encoded_diff


def main(filename: str):
    with open(filename) as file:
        return compute_sum_lenghts(file.read().splitlines())
