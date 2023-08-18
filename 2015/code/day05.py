from re import findall

from tqdm import tqdm


def check_string_validity(string: str):
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

    return all(conditions[0]), all(conditions[1])


def check_string_list(strings: list[str]):
    res = [0, 0]
    for string in tqdm(strings):
        conditions = check_string_validity(string)
        res[0] += conditions[0]
        res[1] += conditions[1]
    return tuple(res)


def main(filename: str):
    with open(filename) as file:
        return check_string_list(file.read().splitlines())
