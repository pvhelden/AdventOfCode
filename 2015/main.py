import re
from math import prod


def day01():
    res = []
    with open('data/day01.txt') as file:
        text = file.read().strip('\n')
        floor = 0
        dic = {'(': 1, ')': -1}
        for index, letter in enumerate(text):
            floor += dic[letter]
            if not len(res) and floor == -1:
                res.append(index + 1)
        res.insert(0, floor)
    return res


def day02():
    paper = 0
    ribbon = 0
    with open('data/day02.txt') as file:
        for box in file.readlines():
            sep1, sep2 = [m.start() for m in re.finditer('x', box)]
            length = int(box[:sep1])
            width = int(box[sep1 + 1:sep2])
            height = int(box[sep2 + 1:-1])  # Don't include newline char
            smallest = sorted([length, width, height])[:2]

            sides = [length * width, width * height, height * length]
            surface = 2 * sum(sides)
            extra = prod(smallest)
            paper += surface + extra

            circ = 2 * sum(smallest)
            volume = length * width * height
            ribbon += circ + volume
        return [paper, ribbon]


def main():
    print("Day 1:", day01())
    print("Day 2:", day02())


if __name__ == '__main__':
    main()
