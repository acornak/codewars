"""
The goal of this exercise is
to convert a string to a new string
where each character in the new string is "("
if that character appears only once in the original string,
or ")" if that character appears more than once.
Ignore capitalization when determining if a character is a duplicate.
Examples:
  "din"      =>  "((("
  "recede"   =>  "()()()"
  "Success"  =>  ")())())"
  "(( @"     =>  "))(("
Notes: Assertion messages may be unclear about what they display
in some languages. If you read "...It Should encode XXX",
the "XXX" is the expected result, not the input!
"""
import unittest


def duplicate_encode(word: str) -> str:
    """
    Replaces each unique character with "(" and each repeating character with ")"
    """
    word = word.lower()
    return "".join(["(" if word.count(char) == 1 else ")" for char in word])


class DuplicateEncoderTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test_1(self):
        """
        Test all unique
        """
        word = "din"
        res = duplicate_encode(word)
        self.assertEqual(res, "(((")

        # test argument mutation
        self.assertAlmostEqual(word, "din")

    def test_2(self):
        """
        Test repeating
        """
        word = "recede"
        res = duplicate_encode(word)
        self.assertEqual(res, "()()()")

        # test argument mutation
        self.assertAlmostEqual(word, "recede")

    def test_3(self):
        """
        Test mixed case
        """
        word = "Success"
        res = duplicate_encode(word)
        self.assertEqual(res, ")())())")

        # test argument mutation
        self.assertAlmostEqual(word, "Success")

    def test_4(self):
        """
        Test other characters
        """
        word = "(( @"
        res = duplicate_encode(word)
        self.assertEqual(res, "))((")

        # test argument mutation
        self.assertAlmostEqual(word, "(( @")

    def test_5(self):
        """
        Random test
        """
        word = "@YSXE xOPxPN LmhZxmqktQa@)qJtX"
        res = duplicate_encode(word)
        self.assertEqual(res, ")(()())()))()()(()))())()()())")

        # test argument mutation
        self.assertAlmostEqual(word, "@YSXE xOPxPN LmhZxmqktQa@)qJtX")

    def test_6(self):
        """
        Random test
        """
        word = ")(()()(()()()"
        res = duplicate_encode(word)
        self.assertEqual(res, ")))))))))))))")

        # test argument mutation
        self.assertAlmostEqual(word, ")(()()(()()()")


if __name__ == "__main__":
    unittest.main()
