from numpy import uint16
from tqdm import tqdm


def apply_instructions(instructions: list[str], signals: dict[(str, int)]):
    with tqdm() as pbar:
        while len(instructions):
            line = instructions.pop(0)
            signal, wire = line.split(' -> ')
            signal = signal.split(' ')
            if line == '1674 -> b' and 'b' in signals:
                pbar.update()
                continue

            # Check if eventual input wires already have a value assigned. If not, do this line later.
            end = False
            for item in signal:
                if not item.isdigit() and not item.isupper() and item not in signals:
                    end = True
            if end:
                instructions.append(line)
                pbar.update()
                continue

            # If eventual input wires already have a value assigned.
            if len(signal) == 1:
                res = signals[signal[0]] if not signal[0].isdigit() else int(signal[0])
            elif len(signal) == 2:  # NOT
                res = ~uint16(signals[signal[1]])
            else:  # len(signal) == 3
                left, oper, right = signal
                left = signals[left] if not left.isdigit() else int(left)
                right = signals[right] if not right.isdigit() else int(right)
                if oper == 'AND':
                    res = left & right
                elif oper == 'OR':
                    res = left | right
                elif oper == 'LSHIFT':
                    res = left << right
                elif oper == 'RSHIFT':
                    res = left >> right
            signals[wire] = res
            pbar.update()


def day07(instructions: list[str]):
    signals1: dict[(str, int)] = dict()
    apply_instructions(instructions.copy(), signals1)
    signals2: dict[(str, int)] = {'b': signals1['a']}
    apply_instructions(instructions, signals2)
    return signals1['a'], signals2['a']


def main(filename: str):
    with open(filename) as file:
        return day07(file.read().splitlines())
