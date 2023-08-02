import hashlib
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
        for index, letter in tqdm(enumerate(text)):
            floor += dic[letter]
            if not len(res) and floor == -1:
                res.append(index + 1)
        res.append(floor)
    return res[1], res[0]


def day02():
    paper = 0
    ribbon = 0
    with open('data/day02.txt') as file:
        for box in tqdm(file.readlines()):
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
        pos_part_1, pos_robot, pos_santa = [[0, 0]] * 3
        char_dic: dict[str, (int, int)] = {'^': (1, 0), '>': (0, 1), '<': (0, -1), 'v': (-1, 0)}
        dic_part_1: dict[(int, int), int] = {(0, 0): 1}
        dic_part_2: dict[(int, int), int] = {(0, 0): 1}
        for index, char in tqdm(enumerate(text)):
            move = char_dic[char]

            # Part 1
            pos_part_1 = sum_tuples(pos_part_1, move)
            dic_part_1.setdefault(pos_part_1, 0)
            dic_part_1[pos_part_1] += 1

            # Part 2
            if index % 2 == 0:
                pos_part_2 = sum_tuples(move, pos_santa)
                pos_santa = pos_part_2
            else:
                pos_part_2 = sum_tuples(move, pos_robot)
                pos_robot = pos_part_2
            dic_part_2.setdefault(pos_part_2, 0)
            dic_part_2[pos_part_2] += 1
    return len(dic_part_1.values()), len(dic_part_2.values())


def day04():
    with open('data/day04.txt') as file:
        key: str = file.readline().strip('\n')
        number = 1
        hex_hash = hashlib.md5(f'{key}{number}'.encode())
        with tqdm() as pbar:
            while not hex_hash.hexdigest().startswith('0' * 5):
                number += 1
                hex_hash = hashlib.md5(f'{key}{number}'.encode())
                pbar.update()
            return number


def main():
    print("Day 1:")
    print(day01())
    print("Day 2:")
    print(day02())
    print("Day 3:")
    print(day03())
    print("Day 4:")
    print(day04())


if __name__ == '__main__':
    main()
