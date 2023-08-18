from tqdm import tqdm


def day06(instructions: list[str]):
    grid1 = [[False] * 1000 for _ in range(1000)]
    grid2 = [[0] * 1000 for _ in range(1000)]
    increments = {'toggle': 2, 'on': 1, 'off': -1}
    for line in tqdm(instructions):
        line = line.split(' ')
        index = 1 if line[0] == 'toggle' else 2
        start, end = [[int(coord) for coord in item.split(',')] for item in line[index::2]]

        for row in range(start[0], end[0] + 1):
            for col in range(start[1], end[1] + 1):
                # Part 1
                grid1[row][col] = not grid1[row][col] if line[index - 1] == 'toggle' else line[index - 1] == "on"

                # Part 2
                grid2[row][col] = max(0, grid2[row][col] + increments[line[index - 1]])
    return sum(sum(row) for row in grid1), sum(sum(row) for row in grid2)


def main(filename: str):
    with open(filename) as file:
        return day06(file.read().splitlines())
