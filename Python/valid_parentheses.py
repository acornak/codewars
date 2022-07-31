"""
Write a function that takes a string of parentheses,
and determines if the order of the parentheses is valid.
The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis,
input may contain any valid ASCII characters.
Furthermore, the input string may be empty and/or not contain any parentheses at all.
Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
"""
import unittest
import re


def valid_parentheses(string: str) -> bool:
    """
    Returns True if all parentheses are closed
    """
    if len(string) == 0:
        return True

    helper_list = []

    for char in re.sub("[^)(]+", "", string):
        if char == "(":
            helper_list.append("(")
        elif len(helper_list) > 0 and helper_list[-1] == "(":
            helper_list.pop(-1)
        else:
            return False

    if len(helper_list) == 0:
        return True

    return False


class ValidParenthesesTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test_1(self):
        """
        Test 1
        """
        string = "()"
        res = valid_parentheses(string)
        self.assertEqual(res, True)

        # test argument mutation
        self.assertEqual(string, "()")

    def test_2(self):
        """
        Test 2
        """
        string = ")(()))"
        res = valid_parentheses(string)
        self.assertEqual(res, False)

        # test argument mutation
        self.assertEqual(string, ")(()))")

    def test_3(self):
        """
        Test 3
        """
        string = "("
        res = valid_parentheses(string)
        self.assertEqual(res, False)

        # test argument mutation
        self.assertEqual(string, "(")

    def test_4(self):
        """
        Test 4
        """
        string = "(())((()())())"
        res = valid_parentheses(string)
        self.assertEqual(res, True)

        # test argument mutation
        self.assertEqual(string, "(())((()())())")

    def test_5(self):
        """
        Test 5
        """
        string = ""
        res = valid_parentheses(string)
        self.assertEqual(res, True)

        # test argument mutation
        self.assertEqual(string, "")

    def test_6(self):
        """
        Test 6
        """
        string = "test"
        res = valid_parentheses(string)
        self.assertEqual(res, True)

        # test argument mutation
        self.assertEqual(string, "test")

    def test_7(self):
        """
        Test 7
        """
        string = "test("
        res = valid_parentheses(string)
        self.assertEqual(res, False)

        # test argument mutation
        self.assertEqual(string, "test(")


if __name__ == "__main__":
    unittest.main()
