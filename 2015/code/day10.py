from tqdm import tqdm


def apply_iterations(sequence: str, iter_n: int):
    for _ in tqdm(range(iter_n)):
        next_seq = ''
        sub_seq = [sequence[0]]
        for char in sequence[1:]:
            if char == sub_seq[0]:
                sub_seq.append(char)
            else:
                next_seq += f'{len(sub_seq)}{sub_seq[0]}'
                sub_seq = [char]
        next_seq += f'{len(sub_seq)}{sub_seq[0]}'
        sequence = next_seq
    return len(sequence)


def main(filename: str):
    with open(filename) as file:
        sequence = file.read().strip('\n')
        return apply_iterations(sequence, 40), apply_iterations(sequence, 50)
