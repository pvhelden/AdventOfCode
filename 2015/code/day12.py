import json
import re

from tqdm import tqdm


def sum_not_red(string: str):
    doc = json.loads(string)
    total = 0
    stack = [doc]
    with tqdm() as pbar:
        while stack:
            current = stack.pop(0)
            if type(current) == dict:
                if 'red' not in current.values():
                    stack.extend(current.values())
            elif type(current) == list:
                stack.extend(current)
            elif type(current) == int:
                total += current
            pbar.update()
    return total


def sum_all(string: str):
    return sum([int(match) for match in re.findall(r'-?\d+', string)])


def main(filename: str):
    with open(filename) as file:
        text = file.read().strip()
        return sum_all(text), sum_not_red(text)
