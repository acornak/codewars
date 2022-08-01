"""
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer
in the range by a dash, '-'. The range includes all integers in the interval including
both endpoints.It is not considered a range unless it spans at least 3 numbers.
For example "12,13,15-17"

Complete the solution so that it takes a list of integers in increasing order and returns
a correctly formatted string in the range format.

Example:

solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python
"""
import unittest


def solution(args: list[int]) -> str:
    """
    Solution
    """
    if len(args) < 3:
        return ",".join(map(str, args))
    res = []
    helper = []
    for i in range(len(args) - 1):
        if args[i + 1] - args[i] == 1:
            helper.extend([args[i], args[i + 1]])
        else:
            if len(helper) >= 3:
                res.append(f"{min(helper)}-{max(helper)}")
            elif len(helper) != 0:
                for number in helper:
                    res.append(number)
            if args[i] not in helper:
                res.append(args[i])
            helper.clear()
    if len(helper) >= 3:
        res.append(f"{min(helper)}-{max(helper)}")
    elif len(helper) != 0:
        for number in helper:
            res.append(number)
    else:
        res.append(args[-1])
    return ",".join(map(str, res))


class RangeExtractionTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test_1(self):
        """
        Test 1
        """
        args = [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
        res = solution(args)
        self.assertEqual(res, "-6,-3-1,3-5,7-11,14,15,17-20")

        # test argument mutation
        self.assertEqual(
            args,
            [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20],
        )

    def test_2(self):
        """
        Test 2
        """
        args = [-3, -2, -1, 2, 10, 15, 16, 18, 19, 20, 22]
        res = solution(args)
        self.assertEqual(res, "-3--1,2,10,15,16,18-20,22")

        # test argument mutation
        self.assertEqual(args, [-3, -2, -1, 2, 10, 15, 16, 18, 19, 20, 22])

    def test_3(self):
        """
        Test 3
        """
        args = [-3, -2]
        res = solution(args)
        self.assertEqual(res, "-3,-2")

        # test argument mutation
        self.assertEqual(args, [-3, -2])


if __name__ == "__main__":
    unittest.main()
    # test = [-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]
    # solution(test)
