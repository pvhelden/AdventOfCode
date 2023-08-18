from re import findall, sub

from tqdm import tqdm


def day08(strings: list[str]):
    code = 0
    memory = 0
    encoded = 0
    for string in tqdm(strings):
        code += len(string)

        # Part 1
        length = len(string) - 2
        matches = findall(r'\\(?:x\w{2}|\\|\")', string)
        for match in matches:
            length -= len(match) - 1
        memory += length

        # Part 2
        encoded += len(sub(r'[\\\"]', '\\\0', string)) + 2
    return code - memory, encoded - code


def main(filename: str):
    with open(filename) as file:
        return day08(file.read().splitlines())
