"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

It's guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.
"""
import unittest


def find_uniq(arr: list[float]) -> float:
    """
    Returns unique element
    """
    if arr[0] != arr[1]:
        if arr[1] != arr[2]:
            return arr[1]
        return arr[0]
    for i in arr[2:]:
        if i != arr[0]:
            return i
    return 0


class UniqueNumberTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test_1(self):
        """
        Test 1
        """
        arr = [1, 1, 1, 2, 1, 1]
        res = find_uniq(arr)
        self.assertEqual(res, 2)

        # test argument mutation
        self.assertEqual(arr, [1, 1, 1, 2, 1, 1])

    def test_2(self):
        """
        Test 2
        """
        arr = [0, 0, 0.55, 0, 0]
        res = find_uniq(arr)
        self.assertEqual(res, 0.55)

        # test argument mutation
        self.assertEqual(arr, [0, 0, 0.55, 0, 0])

    def test_3(self):
        """
        Test 3
        """
        arr = [3, 10, 3, 3, 3]
        res = find_uniq(arr)
        self.assertEqual(res, 10)

        # test argument mutation
        self.assertEqual(arr, [3, 10, 3, 3, 3])


if __name__ == "__main__":
    unittest.main()
