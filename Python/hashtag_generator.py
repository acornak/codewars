"""
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.

Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
"""
import unittest


def generate_hashtag(string: str) -> str | bool:
    """
    Create hashtag from string
    """
    res = "#"

    for word in string.split():
        res += word.capitalize()

    return res if 1 < len(res) < 140 else False


class HashtagGeneratorTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test_1(self):
        """
        Test empty string
        """
        test = ""
        res = generate_hashtag(test)
        self.assertEqual(res, False)

        # test argument mutation
        self.assertEqual(test, "")

    def test_2(self):
        """
        Test simple string
        """
        test = "Codewars"
        res = generate_hashtag(test)
        self.assertEqual(res, "#Codewars")

        # test argument mutation
        self.assertEqual(test, "Codewars")

    def test_3(self):
        """
        Test simple string with unnecessary spaces
        """
        test = "Codewars       "
        res = generate_hashtag(test)
        self.assertEqual(res, "#Codewars")

        # test argument mutation
        self.assertEqual(test, "Codewars       ")

    def test_4(self):
        """
        Test remove spaces only
        """
        test = "Codewars Is Nice"
        res = generate_hashtag(test)
        self.assertEqual(res, "#CodewarsIsNice")

        # test argument mutation
        self.assertEqual(test, "Codewars Is Nice")

    def test_5(self):
        """
        Test remove spaces and capitalize first letter
        """
        test = "codewars is nice"
        res = generate_hashtag(test)
        self.assertEqual(res, "#CodewarsIsNice")

        # test argument mutation
        self.assertEqual(test, "codewars is nice")

    def test_6(self):
        """
        Test lower case all but first letter
        """
        test = "CodeWars is nice"
        res = generate_hashtag(test)
        self.assertEqual(res, "#CodewarsIsNice")

        # test argument mutation
        self.assertEqual(test, "CodeWars is nice")

    def test_7(self):
        """
        Test hashtag at the beginning
        """
        test = "Do We have A Hashtag"
        res = generate_hashtag(test)
        self.assertEqual(res[0], "#")

        # test argument mutation
        self.assertEqual(test, "Do We have A Hashtag")

    def test_8(self):
        """
        Test 1 letter words
        """
        test = "c i n"
        res = generate_hashtag(test)
        self.assertEqual(res, "#CIN")

        # test argument mutation
        self.assertEqual(test, "c i n")

    def test_9(self):
        """
        Test hashtag at the beginning
        """
        test = "Do We have A Hashtag"
        res = generate_hashtag(test)
        self.assertEqual(res[0], "#")

        # test argument mutation
        self.assertEqual(test, "Do We have A Hashtag")

    def test_10(self):
        """
        Test unnecessary middle spaces
        """
        test = "codewars  is  nice"
        res = generate_hashtag(test)
        self.assertEqual(res, "#CodewarsIsNice")

        # test argument mutation
        self.assertEqual(test, "codewars  is  nice")

    def test_11(self):
        """
        Test long hashtag
        """
        test = "Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo"
        test += "oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat"
        res = generate_hashtag(test)
        self.assertEqual(res, False)


if __name__ == "__main__":
    unittest.main()
