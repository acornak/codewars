# pylint: disable=invalid-name
"""
Create a RomanNumerals class that can convert a roman numeral to and from an integer value.
It should follow the API demonstrated in the examples below.
Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting
with the left most digit and skipping any digit with a value of zero.
In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC.
2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each
Roman symbol in descending order: MDCLXVI.

Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

Examples
RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000
Help
Symbol	Value
I	1
IV	4
V	5
X	10
L	50
C	100
D	500
M	1000

https://www.codewars.com/kata/51b66044bce5799a7f000003/python
"""

import unittest


class RomanNumerals:
    """
    Convert number to Roman and vice versa
    """

    @staticmethod
    def to_roman(val: int) -> str:
        """
        Convert from int to Roman
        """
        conversion = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        res = ""
        for conv in conversion:
            res += val // conv[0] * conv[1]
            val = val % conv[0]
            if val == 0:
                break
        return res

    @staticmethod
    def from_roman(roman_num: str) -> int:
        """
        Convert from Roman to int
        """
        singles = [
            (1000, "M"),
            (500, "D"),
            (100, "C"),
            (50, "L"),
            (10, "X"),
            (5, "V"),
            (1, "I"),
        ]
        doubles = [
            (900, "CM"),
            (400, "CD"),
            (90, "XC"),
            (40, "XL"),
            (9, "IX"),
            (4, "IV"),
        ]

        res = 0
        for double in doubles:
            if double[1] in roman_num:
                res += double[0]
                roman_num = roman_num.replace(double[1], "")

        for single in singles:
            res += roman_num.count(single[1]) * single[0]
        return res


class RomanNumeralsTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test_to_roman(self):
        """
        Test int to Roman
        """
        x = 1000
        res = RomanNumerals.to_roman(x)
        self.assertEqual(res, "M")

        x = 4
        res = RomanNumerals.to_roman(x)
        self.assertEqual(res, "IV")

        x = 1
        res = RomanNumerals.to_roman(x)
        self.assertEqual(res, "I")

        x = 1990
        res = RomanNumerals.to_roman(x)
        self.assertEqual(res, "MCMXC")

        x = 2008
        res = RomanNumerals.to_roman(x)
        self.assertEqual(res, "MMVIII")

    def test_from_roman(self):
        """
        Test int to Roman
        """
        x = "XXI"
        res = RomanNumerals.from_roman(x)
        self.assertEqual(res, 21)

        x = "I"
        res = RomanNumerals.from_roman(x)
        self.assertEqual(res, 1)

        x = "IV"
        res = RomanNumerals.from_roman(x)
        self.assertEqual(res, 4)

        x = "MMVIII"
        res = RomanNumerals.from_roman(x)
        self.assertEqual(res, 2008)

        x = "MDCLXVI"
        res = RomanNumerals.from_roman(x)
        self.assertEqual(res, 1666)


if __name__ == "__main__":
    unittest.main()
