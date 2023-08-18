from tqdm import tqdm

from utils import sum_tuples


def find_final_positions(text: str):
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


def main(filename: str):
    with open(filename) as file:
        return find_final_positions(file.read().strip('\n'))
