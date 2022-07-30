"""
Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces.
"""
import unittest


def get_count(sentence: str) -> int:
    """
    Returns number of vowels
    """
    return len([char for char in sentence if char in "aAeEiIoOuU"])


class VowelCountTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test_1(self):
        """
        Test vowels only
        """
        self.assertEqual(get_count("aeiou"), 5)

    def test_2(self):
        """
        Test y only
        """
        self.assertEqual(get_count("y"), 0)

    def test_3(self):
        """
        Test consonants only
        """
        self.assertEqual(get_count("bcdfghjklmnpqrstvwxz y"), 0)

    def test_4(self):
        """
        Test empty string
        """
        self.assertEqual(get_count(""), 0)

    def test_5(self):
        """
        Test word
        """
        self.assertEqual(get_count("abracadabra"), 5)

    def test_6(self):
        """
        Test sentence
        """
        self.assertEqual(get_count("abracadabra and something"), 9)


if __name__ == "__main__":
    unittest.main()
