from math import prod
from re import finditer

from tqdm import tqdm


def get_required_lenghts(boxes: list[str]):
    paper = 0
    ribbon = 0
    for box in tqdm(boxes):
        sep1, sep2 = [m.start() for m in finditer('x', box)]
        length = int(box[:sep1])
        width = int(box[sep1 + 1:sep2])
        height = int(box[sep2 + 1:])  # Don't include newline char
        smallest = sorted([length, width, height])[:2]

        sides = [length * width, width * height, height * length]
        surface = 2 * sum(sides)
        extra = prod(smallest)
        paper += surface + extra

        circ = 2 * sum(smallest)
        volume = length * width * height
        ribbon += circ + volume
    return paper, ribbon


def main(filename: str):
    with open(filename) as file:
        return get_required_lenghts(file.read().splitlines())
