"""
In this kata, you have an input string and you should check whether it is a valid message.
To decide that, you need to split the string by the numbers, and then compare the numbers with
the number of characters in the following substring.

For example "3hey5hello2hi" should be split into 3, hey, 5, hello, 2,
hi and the function should return true,because "hey" is 3 characters,
"hello" is 5, and "hi" is 2; as the numbers and the character counts match, the result is true.

Notes:

Messages are composed of only letters and digits
Numbers may have multiple digits: e.g. "4code13hellocodewars" is a valid message
Every number must match the number of character in the following substring,
otherwise the message is invalid: e.g. "hello5" and "2hi2" are invalid
If the message is an empty string, you should return true

https://www.codewars.com/kata/5fc7d2d2682ff3000e1a3fbc
"""
import re
import unittest


def is_a_valid_message(message: str) -> bool:
    """
    Message validator
    """
    if len(message) == 0:
        return True

    messages = re.findall(r"\d+|[^\W\d_]+", message)

    if len(messages) % 2 != 0:
        return False

    index = 0
    while index < len(messages) - 1:
        try:
            length = int(messages[index])
        except ValueError:
            return False
        if length != len(messages[index + 1]):
            return False
        index += 2
    return True


class MessageValidatorTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test_1(self):
        """
        Test 1
        """
        string = "3hey5hello2hi"
        res = is_a_valid_message(string)
        self.assertEqual(res, True)

        # test argument mutation
        self.assertEqual(string, "3hey5hello2hi")

    def test_2(self):
        """
        Test 2
        """
        string = "4code13hellocodewars"
        res = is_a_valid_message(string)
        self.assertEqual(res, True)

        # test argument mutation
        self.assertEqual(string, "4code13hellocodewars")

    def test_3(self):
        """
        Test 3
        """
        string = "3hey5hello2hi5"
        res = is_a_valid_message(string)
        self.assertEqual(res, False)

        # test argument mutation
        self.assertEqual(string, "3hey5hello2hi5")

    def test_4(self):
        """
        Test 4
        """
        string = "code4hello5"
        res = is_a_valid_message(string)
        self.assertEqual(res, False)

        # test argument mutation
        self.assertEqual(string, "code4hello5")

    def test_5(self):
        """
        Test 5
        """
        string = "1a2bb3ccc4dddd5eeeee"
        res = is_a_valid_message(string)
        self.assertEqual(res, True)

        # test argument mutation
        self.assertEqual(string, "1a2bb3ccc4dddd5eeeee")

    def test_6(self):
        """
        Test 6
        """
        string = ""
        res = is_a_valid_message(string)
        self.assertEqual(res, True)

        # test argument mutation
        self.assertEqual(string, "")


if __name__ == "__main__":
    unittest.main()
