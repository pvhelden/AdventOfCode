import re


def sum_all(string: str):
    return sum([int(match) for match in re.findall(r'-?\d+', string)])


def main(filename: str):
    with open(filename) as file:
        return sum_all(file.read().strip())
