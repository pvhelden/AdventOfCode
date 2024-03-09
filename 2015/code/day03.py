from tqdm import tqdm

from utils import sum_tuples


def find_final_positions(text: str):
    pos_part_1, pos_robot, pos_santa = [[0, 0]] * 3
    char_dic: dict[str, (int, int)] = {'^': (1, 0), '>': (0, 1), '<': (0, -1), 'v': (-1, 0)}
    part_1 = {(0, 0)}
    part_2 = {(0, 0)}
    for index, char in tqdm(enumerate(text)):
        move = char_dic[char]

        # Part 1
        pos_part_1 = sum_tuples(pos_part_1, move)
        part_1.add(pos_part_1)

        # Part 2
        if not index % 2:
            pos_part_2 = sum_tuples(move, pos_santa)
            pos_santa = pos_part_2
        else:
            pos_part_2 = sum_tuples(move, pos_robot)
            pos_robot = pos_part_2
        part_2.add(pos_part_2)
    return len(part_1), len(part_2)


def main(filename: str):
    with open(filename) as file:
        return find_final_positions(file.read().strip('\n'))
