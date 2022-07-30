"""
The Western Suburbs Croquet Club has two categories of membership, Senior and Open.
They would like your help with an application form that will tell prospective members
which category they will be placed.
To be a senior, a member must be at least 55 years old and have a handicap greater than 7.
In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.
Input will consist of a list of pairs. Each pair contains information for a single potential member.
Information consists of an integer for the person's age and an integer for the person's handicap.
Output will consist of a list of string values (in Haskell and C: Open or Senior) stating
whether the respective member is to be placed in the senior or open category.
Example
input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]
"""
import unittest


def open_or_senior(members: list[list[int]]) -> list[str]:
    """
    Returns "Open" if age < 55 or handicap > 7
    """
    return [
        "Senior" if age >= 55 and handicap >= 8 else "Open"
        for (age, handicap) in members
    ]


class CategorizeNewMemberTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test_1(self):
        """
        Test 1
        """
        members = [(45, 12), (55, 21), (19, -2), (104, 20)]
        res = open_or_senior(members)

        self.assertEqual(res, ["Open", "Senior", "Open", "Senior"])

        # test argument mutation
        self.assertAlmostEqual(members, [(45, 12), (55, 21), (19, -2), (104, 20)])

    def test_2(self):
        """
        Test 2
        """
        members = [(16, 23), (73, 1), (56, 20), (1, -1)]
        res = open_or_senior(members)

        self.assertEqual(res, ["Open", "Open", "Senior", "Open"])

        # test argument mutation
        self.assertAlmostEqual(members, [(16, 23), (73, 1), (56, 20), (1, -1)])


if __name__ == "__main__":
    unittest.main()
