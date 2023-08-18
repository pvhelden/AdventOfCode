from tqdm import tqdm


def get_final_floor_number(text: str):
    res = [0, 0]
    floor_nr = 0
    dic = {'(': 1, ')': -1}
    for index, letter in tqdm(enumerate(text)):
        floor_nr += dic[letter]
        if not res[1] and floor_nr == -1:
            res[1] = index + 1
    res[0] = floor_nr
    return tuple(res)


def main(filename: str):
    with open(filename) as file:
        return get_final_floor_number(file.read().strip('\n'))
