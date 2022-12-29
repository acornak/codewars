"""
Can a value be both True and False?

Define omnibool so that it returns True for the following:

omnibool == True and omnibool == False
"""
import unittest


class Omnibool:
    """
    Solution
    """

    def __eq__(self, _):
        """
        Comparison override
        """
        return True


omnibool = Omnibool()


class SchroedingersBooleanTestCase(unittest.TestCase):
    """
    Unit Tests
    """

    def test(self):
        """
        Assertions
        """
        self.assertEqual(omnibool, True)
        self.assertEqual(omnibool, True)
        self.assertEqual(omnibool, False)


if __name__ == "__main__":
    unittest.main()
