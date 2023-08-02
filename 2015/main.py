from hashlib import md5
from math import prod
from re import finditer, findall
from time import sleep

from tqdm import tqdm

from utils import sum_tuples


def day01(text: str):
    res = [0, 0]
    floor = 0
    dic = {'(': 1, ')': -1}
    for index, letter in tqdm(enumerate(text)):
        floor += dic[letter]
        if not res[1] and floor == -1:
            res[1] = index + 1
    res[0] = floor
    return res[0], res[1]


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
        if index % 2 == 0:
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
        return res[0], res[1]


def day05(strings: list[str]):
    res = [0, 0]
    for string in tqdm(strings):
        if any(substring in string for substring in ['ab', 'cd', 'pq', 'xy']):
            continue

        if len(findall(r'[aeiou]', string)) < 3:
            continue

        found = False
        for index in range(len(string) - 1):
            if string[index] == string[index + 1]:
                found = True
                break
        if not found:
            continue

        res[0] += 1
    return res[0], res[1]


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
        print(day05(file.readlines()))


if __name__ == '__main__':
    main()
