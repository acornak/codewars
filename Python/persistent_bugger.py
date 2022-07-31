"""
Write a function, persistence, that takes in a positive parameter num and
returns its multiplicative persistence,which is the number of times you must
multiply the digits in num until you reach a single digit.

For example (Input --> Output):

39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)
"""
import unittest


def multiply_digits(number: int) -> int:
    """
    Multiply digits of a number, return result
    """
    res = 1
    for digit in str(number):
        res *= int(digit)
    return res


def persistence(number: int) -> int:
    """
    Persistence
    """
    if number < 10:
        return 0
    res = 1
    helper = multiply_digits(number)
    while helper >= 10:
        helper = multiply_digits(helper)
        res += 1
    return res


class PersistentBuggerTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test_1(self):
        """
        Test 1
        """
        test = 39
        res = persistence(test)
        self.assertEqual(res, 3)

        # test argument mutation
        self.assertEqual(test, 39)

    def test_2(self):
        """
        Test 2
        """
        test = 4
        res = persistence(test)
        self.assertEqual(res, 0)

        # test argument mutation
        self.assertEqual(test, 4)

    def test_3(self):
        """
        Test 3
        """
        test = 25
        res = persistence(test)
        self.assertEqual(res, 2)

        # test argument mutation
        self.assertEqual(test, 25)

    def test_4(self):
        """
        Test 4
        """
        test = 999
        res = persistence(test)
        self.assertEqual(res, 4)

        # test argument mutation
        self.assertEqual(test, 999)


if __name__ == "__main__":
    unittest.main()
