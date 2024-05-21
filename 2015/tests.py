import unittest

from main import *


class TestAdvent(unittest.TestCase):
    def test_day01(self):
        # Part 1
        self.assertEqual(0, day01.get_final_floor_number('(())')[0])
        self.assertEqual(0, day01.get_final_floor_number('()()')[0])
        self.assertEqual(3, day01.get_final_floor_number('(((')[0])
        self.assertEqual(3, day01.get_final_floor_number('(()(()(')[0])
        self.assertEqual(3, day01.get_final_floor_number('))(((((')[0])
        self.assertEqual(-1, day01.get_final_floor_number('())')[0])
        self.assertEqual(-1, day01.get_final_floor_number('))(')[0])
        self.assertEqual(-3, day01.get_final_floor_number(')))')[0])
        self.assertEqual(-3, day01.get_final_floor_number(')())())')[0])

        # Part 2
        self.assertEqual(1, day01.get_final_floor_number(')')[1])
        self.assertEqual(5, day01.get_final_floor_number('()())')[1])

        # Solution
        self.assertEqual((74, 1795), day01.main('data/day01.txt'))

    def test_day02(self):
        # Parts 1, 2
        self.assertEqual((58, 34), day02.get_required_lenghts(['2x3x4']))
        self.assertEqual((43, 14), day02.get_required_lenghts(['1x1x10']))

        # Solution
        self.assertEqual((1606483, 3842356), day02.main('data/day02.txt'))

    def test_day03(self):
        # Part 1
        self.assertEqual(2, day03.find_final_positions('>')[0])
        self.assertEqual(4, day03.find_final_positions('^>v<')[0])
        self.assertEqual(2, day03.find_final_positions('^v^v^v^v^v')[0])

        # Part 2
        self.assertEqual(3, day03.find_final_positions('^v')[1])
        self.assertEqual(3, day03.find_final_positions('^>v<')[1])
        self.assertEqual(11, day03.find_final_positions('^v^v^v^v^v')[1])

        # Solution
        self.assertEqual((2572, 2631), day03.main('data/day03.txt'))

    def test_day04(self):
        # Part 1
        self.assertEqual(609043, day04.find_zero_padded_hex('abcdef')[0])
        self.assertEqual(1048970, day04.find_zero_padded_hex('pqrstuv')[0])

        # Solution
        self.assertEqual((254575, 1038736), day04.main('data/day04.txt'))

    def test_day05(self):
        # Part 1
        self.assertEqual(1, day05.check_string_validity('ugknbfddgicrmopn')[0])
        self.assertEqual(1, day05.check_string_validity('aaa')[0])
        self.assertEqual(0, day05.check_string_list(['jchzalrnumimnmhp'])[0])
        self.assertEqual(0, day05.check_string_list(['haegwjzuvuyypxyu', 'dvszwmarrgswjxmb'])[0])

        # Part 2
        self.assertEqual(1, day05.check_string_validity('qjhvhtzxzqqjkmpb')[1])
        self.assertEqual(1, day05.check_string_validity('xxyxx')[1])
        self.assertEqual(1, day05.check_string_list(['sknufchjdvccccta', 'sknucbcfchjdvcdcta'])[1])
        self.assertEqual(0, day05.check_string_list(['uurcxstgmygtbstg'])[1])
        self.assertEqual(0, day05.check_string_list(['ieodomkazucvgmuy'])[1])

        # Solution
        self.assertEqual((238, 69), day05.main('data/day05.txt'))

    def test_day06(self):
        # Part 1
        self.assertEqual(1000000, day06.count_lit_lights(['turn on 0,0 through 999,999'])[0])
        self.assertEqual(1000, day06.count_lit_lights(['toggle 0,0 through 999,0'])[0])
        self.assertEqual(96, day06.count_lit_lights(['turn on 495,495 through 504,504',
                                                     'turn off 499,499 through 500,500'])[0])

        # Part 2
        self.assertEqual(1, day06.count_lit_lights(['turn on 0,0 through 0,0'])[1])
        self.assertEqual(2000000, day06.count_lit_lights(['toggle 0,0 through 999,999'])[1])
        self.assertEqual(0, day06.count_lit_lights(['turn off 499,499 through 500,500'])[1])
        self.assertEqual(10, day06.count_lit_lights(['toggle 0,0 through 0,9', 'turn off 0,0 through 0,9'])[1])

        # Solution
        self.assertEqual((377891, 14110788), day06.main('data/day06.txt'))

    def test_day07(self):
        # Part 1
        self.assertEqual(72, day07.compute_signal_a(['123 -> x', '456 -> y', 'x AND y -> a'])[0])
        self.assertEqual(507, day07.compute_signal_a(['123 -> x', '456 -> y', 'x OR y -> a'])[0])
        self.assertEqual(492, day07.compute_signal_a(['123 -> x', 'x LSHIFT 2 -> a'])[0])
        self.assertEqual(114, day07.compute_signal_a(['456 -> y', 'y RSHIFT 2 -> a'])[0])
        self.assertEqual(65412, day07.compute_signal_a(['123 -> x', 'NOT x -> a'])[0])
        self.assertEqual(123, day07.compute_signal_a(['123 -> x', 'x -> a'])[0])
        self.assertEqual(123, day07.compute_signal_a(['x -> a', '123 -> x'])[0])
        self.assertEqual(1, day07.compute_signal_a(['123 -> x', '1 AND x -> a'])[0])

        # Solution
        self.assertEqual((46065, 14134), day07.main('data/day07.txt'))

    def test_day08(self):
        # Parts 1, 2
        self.assertEqual((2, 4), day08.find_lengths_diff(r'""'))
        self.assertEqual((2, 4), day08.compute_sum_lenghts([r'"abc"']))
        self.assertEqual((8, 11), day08.compute_sum_lenghts([r'"aaa\"aaa"', r'"\x27"']))

        # Solution
        self.assertEqual((1371, 2117), day08.main('data/day08.txt'))

    def test_day09(self):
        # Parts 1, 2
        self.assertEqual((605, 982), day09.find_extreme_paths(['London to Dublin = 464',
                                                               'London to Belfast = 518',
                                                               'Dublin to Belfast = 141']))

        # Solution
        self.assertEqual((117, 909), day09.main('data/day09.txt'))

    def test_day10(self):
        # Parts 1, 2
        self.assertEqual(2, day10.apply_iterations('1', iter_n=1))
        self.assertEqual(2, day10.apply_iterations('11', iter_n=1))
        self.assertEqual(4, day10.apply_iterations('21', iter_n=1))
        self.assertEqual(6, day10.apply_iterations('1211', iter_n=1))
        self.assertEqual(6, day10.apply_iterations('111221', iter_n=1))
        self.assertEqual(6, day10.apply_iterations('1', iter_n=5))

        # Solution
        self.assertEqual((329356, 4666278), day10.main('data/day10.txt'))

    def test_day11(self):
        # Parts 1, 2
        self.assertEqual((True, False, False), day11.check_pass([ord(char) for char in 'hijklmmn']))
        self.assertEqual((False, True, False), day11.check_pass([ord(char) for char in 'abbcegjk']))
        self.assertEqual((False, True, True), day11.check_pass([ord(char) for char in 'abbceffg']))
        self.assertEqual((True, True, False), day11.check_pass([ord(char) for char in 'abcaaaaa']))
        self.assertEqual([ord(char) for char in 'baaaaaaa'], day11.incr_pass([ord(char) for char in 'azzzzzzz']))
        self.assertEqual('abcdffaa', day11.find_next_pass('abcdefgh'))
        self.assertEqual('ghjaabcc', day11.find_next_pass('ghijklmn'))

        # Solution
        self.assertEqual(('hxbxxyzz', 'hxcaabcc'), day11.main('data/day11.txt'))

    def test_day12(self):
        # Part 1
        self.assertEqual(6, day12.sum_all('[1,2,3]'))
        self.assertEqual(6, day12.sum_all('{"a":2,"b":4}'))
        self.assertEqual(3, day12.sum_all('[[[3]]]'))
        self.assertEqual(3, day12.sum_all('{"a":{"b":4},"c":-1}'))
        self.assertEqual(0, day12.sum_all('{"a":[-1,1]}'))
        self.assertEqual(0, day12.sum_all('[-1,{"a":1}]'))
        self.assertEqual(0, day12.sum_all('[]'))
        self.assertEqual(0, day12.sum_all('{}'))

        # Part 2
        self.assertEqual(6, day12.sum_not_red('[1,2,3]'))
        self.assertEqual(4, day12.sum_not_red('[1,{"c":"red","b":2},3]'))
        self.assertEqual(0, day12.sum_not_red('{"d":"red","e":[1,2,3,4],"f":5}'))
        self.assertEqual(6, day12.sum_not_red('[1,"red",5]'))

        # Solution
        self.assertEqual((111754, 65402), day12.main('data/day12.txt'))

    def test_day13(self):
        # Part 1
        self.assertEqual(330, day13.find_max_happiness([
            "Alice would gain 54 happiness units by sitting next to Bob.",
            "Alice would lose 79 happiness units by sitting next to Carol.",
            "Alice would lose 2 happiness units by sitting next to David.",
            "Bob would gain 83 happiness units by sitting next to Alice.",
            "Bob would lose 7 happiness units by sitting next to Carol.",
            "Bob would lose 63 happiness units by sitting next to David.",
            "Carol would lose 62 happiness units by sitting next to Alice.",
            "Carol would gain 60 happiness units by sitting next to Bob.",
            "Carol would gain 55 happiness units by sitting next to David.",
            "David would gain 46 happiness units by sitting next to Alice.",
            "David would lose 7 happiness units by sitting next to Bob.",
            "David would gain 41 happiness units by sitting next to Carol."
        ]))

        # Part 2
        self.assertEqual(3, len(day13.parse_happiness_data([
            "Alice would gain 54 happiness units by sitting next to Bob.",
            "Bob would gain 83 happiness units by sitting next to Alice.",
        ], True)))

        # Solution
        self.assertEqual((664, 640), day13.main('data/day13.txt'))

    def test_day14(self):
        # Part 1
        self.assertEqual(1120, day14.find_total_distance(14, 10, 127, 1000))
        self.assertEqual(1056, day14.find_total_distance(16, 11, 162, 1000))
        self.assertEqual(1120, day14.race_distance([
            'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
            'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.',
        ], 1000))

        # Part 2
        self.assertEqual(689, day14.race_score([
            'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
            'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.',
        ], 1000))

        # Solution
        self.assertEqual((2696, 1084), day14.main('data/day14.txt'))

    def test_day15(self):
        # Part 1
        self.assertEqual([-1, -2, 6, 3, 8], day15.get_props(
            'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
        ))
        self.assertEqual(62842880, day15.solve_function([
            'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
            'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3',
        ]))

        # Part 2
        self.assertEqual(57600000, day15.solve_function([
            'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
            'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3',
        ], 500))

        # Solution
        self.assertEqual((222870, 117936), day15.main('data/day15.txt'))

    def test_day16(self):
        # Part 1
        parsed = day16.parse_sues(
            ['Sue 1: children: 1, cars: 8, vizslas: 7', 'Sue 2: akitas: 10, perfumes: 10, children: 5']
        ).rows()
        self.assertEqual(parsed[0][0], 1)
        self.assertEqual(int(parsed[0][2]), 8)
        self.assertEqual(int(parsed[0][4]), 1)
        self.assertEqual(int(parsed[0][10]), 7)
        self.assertEqual(parsed[1][0], 2)
        self.assertEqual(int(parsed[1][1]), 10)
        self.assertEqual(int(parsed[1][4]), 5)
        self.assertEqual(int(parsed[1][6]), 10)
        self.assertEqual(1, day16.find_sue(
            ['Sue 1: children: 1, cars: 8, vizslas: 7', 'Sue 2: akitas: 10, perfumes: 10, children: 5'],
            {'children': 1, 'cars': 8, 'vizslas': 7, 'cats': 0}
        ))

        # Part 2
        self.assertEqual(2, day16.find_sue(
            ['Sue 1: akitas: 7, trees: 8, pomeranians: 4', 'Sue 2: goldfish: 1, perfumes: 4, cars: 6'],
            {'akitas': 7, 'trees': 9, 'pomeranians': 3, 'cats': 0}, False
        ))

        # Solution
        self.assertEqual((213, 323), day16.main('data/day16.txt'))

    def test_day17(self):
        # Part 1
        self.assertEqual([3, 2, 1], day17.parse_containers(['2', '1', '3']))
        self.assertEqual(4, day17.get_number_combinations(['20', '15', '10', '5', '5'], 25))
        self.assertEqual(4, day17.get_number_combinations(['20', '15', '10', '10', '5'], 35))

        # Part 2
        self.assertEqual(3, day17.get_number_shortest_combinations(['20', '15', '10', '5', '5'], 25))

        # Solution
        self.assertEqual((4372, 4), day17.main('data/day17.txt'))

    def test_day18(self):
        # Part 1
        self.assertEqual([[True, False], [True, False]], day18.parse_lights(['#.', '#.']))
        self.assertEqual(4, day18.animate_lights([
            '.#.#.#', '...##.', '#....#', '..#...', '#.#..#', '####..'
        ], 4, False))

        # Part 2
        self.assertEqual(17, day18.animate_lights([
            '##.#.#', '...##.', '#....#', '..#...', '#.#..#', '####.#'
        ], 5, True))

        # Solution
        self.assertEqual((821, 886), day18.main('data/day18.txt'))

    def test_day19(self):
        # Part 1
        test_lines = ['H => HO', 'H => OH', 'O => HH']
        self.assertEqual([('H', 'HO'), ('H', 'OH'), ('O', 'HH')], day19.parse_replacements(test_lines))
        self.assertEqual(4, day19.count_molecules(test_lines, 'HOH'))
        self.assertEqual(7, day19.count_molecules(test_lines, 'HOHOHO'))

        # Part 2
        self.assertEqual({'HH': 'O', 'HO': 'H', 'OH': 'H'}, day19.get_reverse_replacements_dict(test_lines))
        test_lines += ['e => H', 'e => O']
        self.assertEqual(3, day19.count_min_steps(test_lines, 'HOH'))
        self.assertEqual(6, day19.count_min_steps(test_lines, 'HOHOHO'))
        self.assertEqual(10, day19.count_min_steps(test_lines, 'HOHOHOHOHO'))

        # Solution
        self.assertEqual((518, 200), day19.main('data/day19.txt'))

    def test_day20(self):
        # Part 1
        self.assertEqual({1, 2, 3, 4, 6, 12}, day20.find_divisors(12))
        self.assertEqual(1, day20.find_lowest_house_number(10))
        self.assertEqual(2, day20.find_lowest_house_number(30))
        self.assertEqual(3, day20.find_lowest_house_number(40))
        self.assertEqual(4, day20.find_lowest_house_number(70))

        # Part 2
        self.assertEqual({1, 2, 5, 10, 25, 50}, day20.find_divisors(50, 50))
        self.assertEqual({3, 17, 51}, day20.find_divisors(51, 50))
        self.assertEqual({53, 106}, day20.find_divisors(106, 50))
        self.assertEqual(1, day20.find_lowest_house_number(11, 11))
        self.assertEqual(2, day20.find_lowest_house_number(12, 11))

        # Solution
        self.assertEqual((831600, 884520), day20.main('data/day20.txt'))

    def test_day21(self):
        # Part 1
        self.assertEqual([10, 9, 8], day21.parse_character('10 9 8'))
        self.assertEqual(True, day21.fight([8, 5, 5], [12, 7, 2]))
        self.assertEqual(False, day21.fight([8, 5, 5], [13, 7, 2]))
        self.assertEqual(True, day21.fight([100, 5, 0], [100, 5, 0]))
        self.assertEqual(8, day21.get_lowest_winning_cost([4, 0, 0]))
        self.assertEqual(10, day21.get_lowest_winning_cost([100, 5, 0]))
        self.assertEqual(23, day21.get_lowest_winning_cost([101, 5, 0]))

        # Part 2

        # Solution
        self.assertEqual((121, None), day21.main('data/day21.txt'))


if __name__ == '__main__':
    unittest.main()
