"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word.
Leave punctuation marks untouched.
"""
import unittest


def pig_it(text: str) -> str:
    """
    Pig word
    """
    word = ""
    res = ""
    for char in text:
        if char.isalpha():
            word += char
        else:
            if len(word) != 0:
                res += word[1:] + word[0] + "ay"
                word = ""
            res += char
    if len(word) != 0:
        res += word[1:] + word[0] + "ay"

    return res


class ComplementaryDNATestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test_1(self):
        """
        Test 1
        """
        text = "Pig latin is cool"
        res = pig_it(text)
        self.assertEqual(res, "igPay atinlay siay oolcay")

        # test argument mutation
        self.assertEqual(text, "Pig latin is cool")

    def test_2(self):
        """
        Test 2
        """
        text = "This is my string!"
        res = pig_it(text)
        self.assertEqual(res, "hisTay siay ymay tringsay!")

        # test argument mutation
        self.assertEqual(text, "This is my string!")

    def test_3(self):
        """
        Test 3
        """
        text = "Hello world !"
        res = pig_it(text)
        self.assertEqual(res, "elloHay orldway !")

        # test argument mutation
        self.assertEqual(text, "Hello world !")

    def test_4(self):
        """
        Test short string
        """
        text = "I"
        res = pig_it(text)
        self.assertEqual(res, "Iay")

        # test argument mutation
        self.assertEqual(text, "I")

    def test_5(self):
        """
        Test non-letters only
        """
        text = "!!!!"
        res = pig_it(text)
        self.assertEqual(res, "!!!!")

        # test argument mutation
        self.assertEqual(text, "!!!!")

    def test_6(self):
        """
        Test multiple sentences
        """
        text = "This is first sentence. This is second."
        res = pig_it(text)
        self.assertEqual(res, "hisTay siay irstfay entencesay. hisTay siay econdsay.")

        # test argument mutation
        self.assertEqual(text, "This is first sentence. This is second.")


if __name__ == "__main__":
    unittest.main()
    # pig_it("This auto is my string!")
