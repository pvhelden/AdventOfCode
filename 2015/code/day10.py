from tqdm import tqdm


def day10(sequence: str, iter_n=50):
    seq1 = ''
    for index in tqdm(range(iter_n)):
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
        if iter_n == 50 and index == 39:
            seq1 = sequence
    return len(seq1) if seq1 else len(sequence), len(sequence)


def main(filename: str):
    with open(filename) as file:
        return day10(file.read().strip('\n'))
