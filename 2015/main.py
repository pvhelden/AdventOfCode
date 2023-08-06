from hashlib import md5
from math import prod
from re import finditer, findall
from time import sleep

from scipy import sparse
from tqdm import tqdm

from utils import sum_tuples


def day01(text: str):
    res = [0, 0]
    floor_nr = 0
    dic = {'(': 1, ')': -1}
    for index, letter in tqdm(enumerate(text)):
        floor_nr += dic[letter]
        if not res[1] and floor_nr == -1:
            res[1] = index + 1
    res[0] = floor_nr
    return tuple(res)


def day02(boxes: list[str]):
    paper = 0
    ribbon = 0
    for box in tqdm(boxes):
        box = box.strip('\n')
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


def day03(text: str):
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
        if not index % 2:
            pos_part_2 = sum_tuples(move, pos_santa)
            pos_santa = pos_part_2
        else:
            pos_part_2 = sum_tuples(move, pos_robot)
            pos_robot = pos_part_2
        dic_part_2.setdefault(pos_part_2, 0)
        dic_part_2[pos_part_2] += 1
    return len(dic_part_1.values()), len(dic_part_2.values())


def day04(key: str):
    res = [0, 0]
    number = 1
    with tqdm() as pbar:
        while not res[0] or not res[1]:
            number += 1
            hex_hash = md5(f'{key}{number}'.encode())
            if not res[0] and hex_hash.hexdigest().startswith('0' * 5):
                res[0] = number
            if not res[1] and hex_hash.hexdigest().startswith('0' * 6):
                res[1] = number
            pbar.update()
        return tuple(res)


def day05(strings: list[str]):
    res = [0, 0]
    for string in tqdm(strings):
        conditions = [[False, False, False], [False, False]]

        # Part 1
        conditions[0][0] = len(findall(r'[aeiou]', string)) >= 3
        conditions[0][1] = any([i == j for i, j in zip(string, string[1:])])
        conditions[0][2] = not any(substring in string for substring in ['ab', 'cd', 'pq', 'xy'])

        # Part 2
        valid_triples = [i + j + k for i, j, k in zip(string, string[1:], string[2:]) if i == k]
        if len(valid_triples) != len({*valid_triples}):
            conditions[1][0] = True
        else:
            valid_pairs = [i + j for i, j, k in zip(string, string[1:], string[2:] + '0') if not i == j == k]
            conditions[1][0] = len(valid_pairs) != len({*valid_pairs})
        conditions[1][1] = any(valid_triples)

        res[0] += all(conditions[0])
        res[1] += all(conditions[1])
    return tuple(res)


def day06(instructions: list[str]):
    grid1 = sparse.lil_array((1000, 1000), dtype='bool')
    grid2 = sparse.lil_array((1000, 1000), dtype='int')
    for line in tqdm(instructions):
        line = line.split(' ')
        index = 1 if line[0] == "toggle" else 2
        start, end = [[int(coord) for coord in item.split(',')] for item in line[index::2]]
        before = grid1[start[0]:end[0] + 1, start[1]:end[1] + 1]

        # Part 1
        if line[0] == "toggle":
            inplace1 = [[not item for item in row] for row in before.todense()]
        else:
            inplace1 = line[1] == "on"
        grid1[start[0]:end[0] + 1, start[1]:end[1] + 1] = inplace1

        # Part 2
        diff = {"toggle": 2, "on": 1, "off": -1}[line[index - 1]]
        inplace2 = [[max(0, item + diff) for item in row] for row in before.todense()]
        grid2[start[0]:end[0] + 1, start[1]:end[1] + 1] = inplace2
    return grid1.count_nonzero(), grid2.sum()


def main():
    print("Day 1:")
    with open('data/day01.txt') as file:
        print(day01(file.read().strip('\n')))

    sleep(1)
    print("Day 2:")
    with open('data/day02.txt') as file:
        print(day02(file.readlines()))

    sleep(1)
    print("Day 3:")
    with open('data/day03.txt') as file:
        print(day03(file.read().strip('\n')))

    sleep(1)
    print("Day 4:")
    with open('data/day04.txt') as file:
        print(day04(file.readline().strip('\n')))

    sleep(1)
    print("Day 5:")
    with open('data/day05.txt') as file:
        print(day05(file.read().splitlines()))

    sleep(1)
    print("Day 6:")
    with open('data/day06.txt') as file:
        print(day06(file.read().splitlines()))


if __name__ == '__main__':
    main()
