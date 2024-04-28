def parse_lights(lines: [str]) -> [[int]]:
    return [[True if char == '#' else False for char in list(line)] for line in lines]


def count_neighbours(lights: [[int]], x: int, y: int) -> int:
    count = 0
    for i in range(max(0, x - 1), min(len(lights[0]), x + 2)):
        for j in range(max(0, y - 1), min(len(lights), y + 2)):
            if not (i == x and j == y):
                count += 1 if lights[i][j] else 0
    return count


def next_step(lights: [[int]]) -> None:
    changes = []
    for i, row in enumerate(lights):
        for j, light in enumerate(row):
            count = count_neighbours(lights, i, j)
            if count == 3:
                changes.append((i, j, True))
            elif count != 2:
                changes.append((i, j, False))
    for change in changes:
        lights[change[0]][change[1]] = change[2]


def animate_lights(lines: [str], steps: int) -> int:
    lights = parse_lights(lines)
    for _ in range(steps):
        next_step(lights)
    return sum(sum(row) for row in lights)


def main(filename: str) -> tuple:
    with open(filename) as file:
        lines = file.read().splitlines()
        return animate_lights(lines, 100), None
