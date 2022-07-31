"""
Welcome.

In this kata you are required to, given a string,
replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return
"20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
 ( as a string )
"""
import unittest
from string import ascii_lowercase


def alphabet_position(text: str) -> str:
    """
    Returns letter alphabet position
    """
    return " ".join(
        str(ascii_lowercase.index(letter.lower()) + 1)
        for letter in text
        if letter.isalpha()
    )


class AlphabetPositionTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test_1(self):
        """
        Test 1
        """
        test = "The sunset sets at twelve o' clock."
        res = alphabet_position(test)
        self.assertEqual(
            res,
            "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11",
        )

        # test argument mutation
        self.assertEqual(test, "The sunset sets at twelve o' clock.")

    def test_2(self):
        """
        Test 2
        """
        test = "The narwhal bacons at midnight."
        res = alphabet_position(test)
        self.assertEqual(
            res,
            "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20",
        )

        # test argument mutation
        self.assertEqual(test, "The narwhal bacons at midnight.")


if __name__ == "__main__":
    unittest.main()
