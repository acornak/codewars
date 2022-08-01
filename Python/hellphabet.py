"""
Define a variable ALPHABET that contains the (english) alphabet in lowercase.


Too simple? Well, you can only use the following characters set:

 abcdefghijklmnopqrstuvwxyz(). space included

You code must starts with ALPHABET =  then respects the charset limitation.

Ofc you wouldn't cheat by importing the string module or using eval/exec...
"""
import unittest

# Solution #1 (cheating):
import string

ALPHABET1 = string.ascii_lowercase

# Solution #2 (still cheating because of the numbers):
ALPHABET2 = str().join(list(chr(char) for char in range(97, 123)))


# Solution #3 (the only solution):
ALPHABET3 = str().join(c for c in sorted(set(repr(vars()))) if c.islower())


class HellphabetTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test_solution_1(self):
        """
        Test first solution
        """
        self.assertEqual(ALPHABET1, "abcdefghijklmnopqrstuvwxyz")

    def test_solution_2(self):
        """
        Test second solution
        """
        self.assertEqual(ALPHABET2, "abcdefghijklmnopqrstuvwxyz")

    def test_solution_3(self):
        """
        Test third solution
        """
        self.assertEqual(ALPHABET3, "abcdefghijklmnopqrstuvwxyz")


if __name__ == "__main__":
    unittest.main()
