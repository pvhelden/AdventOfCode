import unittest

from main import day01, day02, day03, day04, day05


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


if __name__ == '__main__':
    unittest.main()
