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
        sentence = "Welcome"
        res = spin_words(sentence)
        self.assertEqual(res, "emocleW")

        # test argument mutation
        self.assertEqual(sentence, "Welcome")

    def test_2(self):
        """
        Test 1 word string
        """
        sentence = "to"
        res = spin_words(sentence)
        self.assertEqual(res, "to")

        # test argument mutation
        self.assertEqual(sentence, "to")

    def test_3(self):
        """
        Test 1 word string
        """
        sentence = "CodeWars"
        res = spin_words(sentence)
        self.assertEqual(res, "sraWedoC")

        # test argument mutation
        self.assertEqual(sentence, "CodeWars")

    def test_4(self):
        """
        Test multiple words string
        """
        sentence = "Hey fellow warriors"
        res = spin_words(sentence)
        self.assertEqual(res, "Hey wollef sroirraw")

        # test argument mutation
        self.assertEqual(sentence, "Hey fellow warriors")

    def test_5(self):
        """
        Test multiple words string
        """
        sentence = "This sentence is a sentence"
        res = spin_words(sentence)
        self.assertEqual(res, "This ecnetnes is a ecnetnes")

        # test argument mutation
        self.assertEqual(sentence, "This sentence is a sentence")


if __name__ == "__main__":
    unittest.main()
