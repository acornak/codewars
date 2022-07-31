"""
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1
foobar23 -> foobar24
foo0042 -> foo0043
foo9 -> foo10
foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
"""
import unittest
import re


def increment_string(string: str) -> str:
    """
    Increment string by 1
    """
    splitted = re.findall(r"\d+|[^\W\d_]+", string)

    if len(string) == 0:
        return "1"

    try:
        last_number = int(splitted[-1])
    except ValueError:
        return string + "1"

    if len(splitted[-1]) >= len(str(last_number + 1)) > len(str(last_number)):
        return string[: -(len(str(last_number)) + 1)] + str(last_number + 1)

    return string[: -len(str(last_number))] + str(last_number + 1)


class MessageValidatorTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test_1(self):
        """
        Test 1
        """
        string = "foo"
        res = increment_string(string)
        self.assertEqual(res, "foo1")

        # test argument mutation
        self.assertEqual(string, "foo")

    def test_2(self):
        """
        Test 2
        """
        string = "foobar001"
        res = increment_string(string)
        self.assertEqual(res, "foobar002")

        # test argument mutation
        self.assertEqual(string, "foobar001")

    def test_3(self):
        """
        Test 3
        """
        string = "foobar1"
        res = increment_string(string)
        self.assertEqual(res, "foobar2")

        # test argument mutation
        self.assertEqual(string, "foobar1")

    def test_4(self):
        """
        Test 4
        """
        string = "foobar0009"
        res = increment_string(string)
        self.assertEqual(res, "foobar0010")

        # test argument mutation
        self.assertEqual(string, "foobar0009")


if __name__ == "__main__":
    # unittest.main()
    print(increment_string("foobar0009"))
