from tqdm import tqdm


def check_straight(password: list[int]):
    # Condition 1
    for code1, code2, code3 in zip(password, password[1:], password[2:]):
        if code1 == code2 - 1 == code3 - 2:
            return True
    return False


def check_confusing(password: list[int]):
    # Condition 2
    return not any([char in password for char in [105, 108, 111]])  # ['i', 'l', 'o']]


def check_pairs(password: list[int]):
    # Condition 3
    pairs = set()
    skip_next = False
    for code1, code2 in zip(password, password[1:]):
        if skip_next:
            skip_next = False
            continue
        if code1 == code2:
            pairs.add(code1)
            skip_next = True
    return len(pairs) == 2


def check_pass(password: list[int]):
    return check_straight(password), check_confusing(password), check_pairs(password)


def incr_pass(new_pass: list[int]):
    done = False
    index = -1
    while not done:
        if new_pass[index] == 122:  # 'z'
            new_pass[index] = 97
            index -= 1
        else:
            new_pass[index] += 1
            done = True
    return new_pass


def find_next_pass(old_pass: str):
    new_pass = [ord(char) for char in old_pass]
    new_pass = incr_pass(new_pass)
    checks = check_pass(new_pass)
    with tqdm() as pbar:
        while not all(checks):
            if not checks[1]:
                for index, code in enumerate(new_pass):
                    if code in [105, 108, 111]:  # ['i', 'l', 'o']
                        new_pass[index] = code + 1
                        new_pass[index + 1:] = [97] * (7 - index)  # ['a']
                        break
            elif not checks[0] or not checks[2]:
                new_pass = incr_pass(new_pass)
            checks = check_pass(new_pass)
            pbar.update()
    return ''.join([chr(code) for code in new_pass])


def main(filename: str):
    with open(filename) as file:
        second = find_next_pass(file.read().strip('\n'))
        third = find_next_pass(second)
        return second, third
