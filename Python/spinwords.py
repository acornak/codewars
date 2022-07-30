"""
Write a function that takes in a string of one or more words, and returns the same string,
but with all five or more letter words reversed (Just like the name of this Kata).
Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.

Examples:

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
spinWords( "This is a test") => returns "This is a test"
spinWords( "This is another test" )=> returns "This is rehtona test"
"""
import unittest


def spin_words(sentence: str) -> str:
    """
    Returns
    """
    return " ".join(
        [word[::-1] if len(word) >= 5 else word for word in sentence.split(" ")]
    )


class SpinwordsTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test_1(self):
        """
        Test 1 word string
        """
        self.assertEqual(spin_words("Welcome"), "emocleW")

    def test_2(self):
        """
        Test 1 word string
        """
        self.assertEqual(spin_words("to"), "to")

    def test_3(self):
        """
        Test 1 word string
        """
        self.assertEqual(spin_words("CodeWars"), "sraWedoC")

    def test_4(self):
        """
        Test 1 word string
        """
        self.assertEqual(spin_words("to"), "to")

    def test_5(self):
        """
        Test multiple words string
        """
        self.assertEqual(spin_words("Hey fellow warriors"), "Hey wollef sroirraw")

    def test_6(self):
        """
        Test multiple words string
        """
        self.assertEqual(
            spin_words("This sentence is a sentence"), "This ecnetnes is a ecnetnes"
        )


if __name__ == "__main__":
    unittest.main()
