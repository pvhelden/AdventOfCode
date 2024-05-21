from time import sleep

from code import (day01, day02, day03, day04, day05, day06, day07, day08, day09, day10, day11, day12, day13, day14,
                  day15, day16, day17, day18, day19, day20, day21)


def main():
    modules = [day01, day02, day03, day04, day05, day06, day07, day08, day09, day10, day11, day12, day13, day14, day15,
               day16, day17, day18, day19, day20, day21]
    days = [i + 1 for i in range(len(modules))]

    for day in days:
        print()
        print(f"Day {day:02}:")
        print(modules[day - 1].main(f'data/day{day:02}.txt'))
        if day != days[-1]:
            sleep(1)


if __name__ == '__main__':
    main()
