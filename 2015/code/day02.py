from math import prod

from tqdm import tqdm


def get_required_lenghts(boxes: list[str]):
    paper = 0
    ribbon = 0
    for box in tqdm(boxes):
        parts = box.split('x')
        length, width, height = [int(part) for part in parts]
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
