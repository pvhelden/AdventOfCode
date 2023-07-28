import re
from math import prod

from tqdm import tqdm

from utils import sum_tuples


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
        res.append(floor)
    return res[1], res[0]


def day02():
    paper = 0
    ribbon = 0
    with open('data/day02.txt') as file:
        for box in file.readlines():
            box = box.strip('\n')
            sep1, sep2 = [m.start() for m in re.finditer('x', box)]
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


def day03():
    with open('data/day03.txt') as file:
        text = file.read().strip('\n')
        pos = [0, 0]
        char_dic: dict[str, (int, int)] = {'^': (1, 0), '>': (0, 1), '<': (0, -1), 'v': (-1, 0)}
        dic: dict[(int, int), int] = {(0, 0): 1}
        for index, char in tqdm(enumerate(text)):
            move = char_dic[char]
            pos = sum_tuples(pos, move)
            dic.setdefault(pos, 0)
            dic[pos] += 1
    return len(dic.values())


def main():
    print("Day 1:", day01())
    print("Day 2:", day02())
    print("Day 3:", day03())


if __name__ == '__main__':
    main()
