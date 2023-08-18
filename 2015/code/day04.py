from hashlib import md5

from tqdm import tqdm


def find_zero_padded_hex(key: str):
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


def main(filename: str):
    with open(filename) as file:
        return find_zero_padded_hex(file.read().strip('\n'))
