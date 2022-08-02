"""
Write a function, which takes a non-negative integer (seconds) as input
and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
https://www.codewars.com/kata/52685f7382004e774f0001f7
"""
import unittest


def make_readable(seconds: int) -> str:
    """
    Takes time in seconds, returns human readable format
    """
    return f"{(seconds // 3600):02d}:{(seconds // 60 % 60):02d}:{(seconds % 60):02d}"


class HumanReadableTimeTestCase(unittest.TestCase):
    """
    Unit Tests
    """

    def test_1(self):
        """
        Test 1
        """
        test = 0
        res = make_readable(test)
        self.assertEqual(res, "00:00:00")

        # test argument mutation
        self.assertEqual(test, 0)

    def test_2(self):
        """
        Test 2
        """
        test = 5
        res = make_readable(test)
        self.assertEqual(res, "00:00:05")

        # test argument mutation
        self.assertEqual(test, 5)

    def test_3(self):
        """
        Test 3
        """
        test = 60
        res = make_readable(test)
        self.assertEqual(res, "00:01:00")

        # test argument mutation
        self.assertEqual(test, 60)

    def test_4(self):
        """
        Test 4
        """
        test = 86399
        res = make_readable(test)
        self.assertEqual(res, "23:59:59")

        # test argument mutation
        self.assertEqual(test, 86399)

    def test_5(self):
        """
        Test 5
        """
        test = 359999
        res = make_readable(test)
        self.assertEqual(res, "99:59:59")

        # test argument mutation
        self.assertEqual(test, 359999)


if __name__ == "__main__":
    unittest.main()
