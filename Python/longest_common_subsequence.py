"""
from Wikipedia:
The longest common subsequence (LCS) problem is the problem of finding the longest subsequence
common to all sequences in a set of sequences.
It differs from problems of finding common substrings: unlike substrings,
subsequences are not required to occupy consecutive positions within the original sequences.

Task
Write a function lcs that accepts two strings and returns their longest common
subsequence as a string.Performance matters.

Examples
lcs( "abcdef", "abc" ) => "abc"
lcs( "abcdef", "acf" ) => "acf"
lcs( "132535365", "123456789" ) => "12356"
lcs( "abcdefghijklmnopq", "apcdefghijklmnobq" ) => "acdefghijklmnoq"
Testing
This is a performance version of xDranik's kata of the same name.
This kata, however, has much more full and heavy testing.
Intermediate random tests have string arguments of 20 characters;
hard random tests 40 characters; extreme 60 characters
(characters are chosen out of 36 different ones).

Notes
The subsequences of "abc" are "", "a", "b", "c", "ab", "ac", "bc", "abc".
"" is a valid subsequence in this kata, and a possible return value.
All inputs will be valid.
Two strings may have more than one longest common subsequence. When this occurs, return any of them.

lcs( string0, string1 ) === lcs( string1, string0 )
Wikipedia has an article that may be helpful.

https://www.codewars.com/kata/593ff8b39e1cc4bae9000070
"""
import unittest
import timeout_decorator

GLOBAL_TIMEOUT = 1


def lcs(string1: str, string2: str) -> str:
    """
    Returns longest common subsequence
    """
    # check the obvious
    if len(string1) == 0 or len(string2) == 0:
        return ""
    # create empty matrix based on length of both strings
    helper = [["" for _ in range(len(string2))] for _ in range(len(string1))]

    # build the matrix
    for i, char1 in enumerate(string1):
        for j, char2 in enumerate(string2):
            if char1 == char2:
                if i == 0 or j == 0:
                    helper[i][j] = char1
                else:
                    helper[i][j] = helper[i - 1][j - 1] + char1
            else:
                helper[i][j] = max(helper[i - 1][j], helper[i][j - 1], key=len)
    return helper[-1][-1]


class LongestCommonSubsequenceTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test_1(self):
        """
        Test 1
        """
        self.assertEqual(lcs("", ""), "")
        self.assertEqual(lcs("abc", ""), "")
        self.assertEqual(lcs("", "abc"), "")
        self.assertEqual(lcs("a", "b"), "")
        self.assertEqual(lcs("a", "a"), "a")
        self.assertEqual(lcs("abc", "a"), "a")
        self.assertEqual(lcs("abc", "ac"), "ac")
        self.assertEqual(lcs("abcdef", "abc"), "abc")
        self.assertEqual(lcs("abcdef", "acf"), "acf")
        self.assertEqual(lcs("anothertest", "notatest"), "nottest")
        self.assertEqual(lcs("132535365", "123456789"), "12356")
        self.assertEqual(lcs("nothardlythefinaltest", "zzzfinallyzzz"), "final")
        self.assertEqual(
            lcs("abcdefghijklmnopq", "apcdefghijklmnobq"), "acdefghijklmnoq"
        )


if __name__ == "__main__":
    timeout_decorator.timeout(GLOBAL_TIMEOUT)(unittest.main)()
    # print(lcs("anothertest", "notatest"))
