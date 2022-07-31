"""
We want to create a function that will add numbers together when called in succession.

add(1)(2) # equals 3
We also want to be able to continue to add numbers to our chain.

add(1)(2)(3) # 6
add(1)(2)(3)(4); # 10
add(1)(2)(3)(4)(5) # 15
and so on.

A single call should be equal to the number passed in.

add(1) # 1
We should be able to store the returned values and reuse them.

addTwo = add(2)
addTwo # 2
addTwo + 5 # 7
addTwo(3) # 5
addTwo(3)(5) # 10
We can assume any number being passed in will be valid whole number.
"""
import unittest


class Add(int):
    """
    Pythonic hack to call "func" in succession
    """

    def __call__(self, number: int) -> int:
        return Add(self + number)


class ChainAddingFunctionTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test_1(self):
        """
        Test 1
        """
        test = 1
        res = Add(test)
        self.assertEqual(res, 1)

        # test argument mutation
        self.assertEqual(test, 1)

    def test_2(self):
        """
        Test 2
        """
        res = Add(1)(2)
        self.assertEqual(res, 3)

    def test_3(self):
        """
        Test 3
        """
        res = Add(1)(2)(3)
        self.assertEqual(res, 6)


if __name__ == "__main__":
    unittest.main()
