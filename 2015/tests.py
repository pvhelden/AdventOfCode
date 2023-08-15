import unittest

from main import day01, day02, day03, day04, day05, day06, day07, day08


class TestAdvent(unittest.TestCase):
    def test_day01(self):
        # Part 1
        self.assertEqual(0, day01('(())')[0])
        self.assertEqual(0, day01('()()')[0])
        self.assertEqual(3, day01('(((')[0])
        self.assertEqual(3, day01('(()(()(')[0])
        self.assertEqual(3, day01('))(((((')[0])
        self.assertEqual(-1, day01('())')[0])
        self.assertEqual(-1, day01('))(')[0])
        self.assertEqual(-3, day01(')))')[0])
        self.assertEqual(-3, day01(')())())')[0])

        # Part 2
        self.assertEqual(1, day01(')')[1])
        self.assertEqual(5, day01('()())')[1])

    def test_day02(self):
        # Part 1
        self.assertEqual(58, day02(['2x3x4'])[0])
        self.assertEqual(43, day02(['1x1x10'])[0])

        # Part 2
        self.assertEqual(34, day02(['2x3x4'])[1])
        self.assertEqual(14, day02(['1x1x10'])[1])

    def test_day03(self):
        # Part 1
        self.assertEqual(2, day03('>')[0])
        self.assertEqual(4, day03('^>v<')[0])
        self.assertEqual(2, day03('^v^v^v^v^v')[0])

        # Part 2
        self.assertEqual(3, day03('^v')[1])
        self.assertEqual(3, day03('^>v<')[1])
        self.assertEqual(11, day03('^v^v^v^v^v')[1])

    def test_day04(self):
        # Part 1
        self.assertEqual(609043, day04('abcdef')[0])
        self.assertEqual(1048970, day04('pqrstuv')[0])

    def test_day05(self):
        # Part 1
        self.assertEqual(1, day05(['ugknbfddgicrmopn'])[0])
        self.assertEqual(1, day05(['aaa'])[0])
        self.assertEqual(0, day05(['jchzalrnumimnmhp'])[0])
        self.assertEqual(0, day05(['haegwjzuvuyypxyu'])[0])
        self.assertEqual(0, day05(['dvszwmarrgswjxmb'])[0])

        # Part 2
        self.assertEqual(1, day05(['qjhvhtzxzqqjkmpb'])[1])
        self.assertEqual(1, day05(['xxyxx'])[1])
        self.assertEqual(1, day05(['sknufchjdvccccta'])[1])
        self.assertEqual(0, day05(['sknucbcfchjdvcdcta'])[1])
        self.assertEqual(0, day05(['uurcxstgmygtbstg'])[1])
        self.assertEqual(0, day05(['ieodomkazucvgmuy'])[1])

    def test_day06(self):
        # Part 1
        self.assertEqual(1000000, day06(['turn on 0,0 through 999,999'])[0])
        self.assertEqual(1000, day06(['toggle 0,0 through 999,0'])[0])
        self.assertEqual(96, day06(['turn on 495,495 through 504,504', 'turn off 499,499 through 500,500'])[0])

        # Part 2
        self.assertEqual(1, day06(['turn on 0,0 through 0,0'])[1])
        self.assertEqual(2000000, day06(['toggle 0,0 through 999,999'])[1])
        self.assertEqual(0, day06(['turn off 499,499 through 500,500'])[1])
        self.assertEqual(10, day06(['toggle 0,0 through 0,9', 'turn off 0,0 through 0,9'])[1])

    def test_day07(self):
        # Part 1
        self.assertEqual(72, day07(['123 -> x', '456 -> y', 'x AND y -> a'])[0])
        self.assertEqual(507, day07(['123 -> x', '456 -> y', 'x OR y -> a'])[0])
        self.assertEqual(492, day07(['123 -> x', 'x LSHIFT 2 -> a'])[0])
        self.assertEqual(114, day07(['456 -> y', 'y RSHIFT 2 -> a'])[0])
        self.assertEqual(65412, day07(['123 -> x', 'NOT x -> a'])[0])
        self.assertEqual(123, day07(['123 -> x', 'x -> a'])[0])
        self.assertEqual(123, day07(['x -> a', '123 -> x'])[0])
        self.assertEqual(1, day07(['123 -> x', '1 AND x -> a'])[0])

    def test_day08(self):
        # Part 1
        self.assertEqual(2 - 0, day08([r'""'])[0])
        self.assertEqual(5 - 3, day08([r'"abc"'])[0])
        self.assertEqual(10 - 7, day08([r'"aaa\"aaa"'])[0])
        self.assertEqual(6 - 1, day08([r'"\x27"'])[0])


if __name__ == '__main__':
    unittest.main()
