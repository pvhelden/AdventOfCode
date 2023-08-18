from time import sleep

from code import day01, day02, day03, day04, day05, day06, day07, day08, day09, day10


def main():
    modules = [day01, day02, day03, day04, day05, day06, day07, day08, day09, day10]
    days = [i + 1 for i in range(len(modules))]
    # days = [2]

    for day in days:
        if not day == 1:
            sleep(1)
        print()
        print(f"Day {day:02}:")
        print(modules[day - 1].main(f'data/day{day:02}.txt'))


if __name__ == '__main__':
    main()
