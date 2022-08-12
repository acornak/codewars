# pylint: disable=invalid-name
"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values
will result in a hexadecimal representation being returned.
Valid decimalvalues for RGB are 0 - 255.
Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3

https://www.codewars.com/kata/513e08acc600c94f01000001/go
"""
import unittest


def validate(val: int) -> int:
    """
    Handle RGB values: should be within range <0, 255>
    """
    if val < 0:
        return 0
    elif val > 255:
        return 255
    return val


def rgb(r: int, g: int, b: int) -> str:
    """
    Convert RGB to hexadecimal
    """
    return f"{validate(r):02X}{validate(g):02X}{validate(b):02X}"


class ComplementaryDNATestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test_1(self):
        """
        Testing zero values
        """
        r, g, b = (0, 0, 0)
        res = rgb(r, g, b)
        self.assertEqual(res, "000000")

    def test_2(self):
        """
        Testing near zero values
        """
        r, g, b = (1, 2, 3)
        res = rgb(r, g, b)
        self.assertEqual(res, "010203")

    def test_3(self):
        """
        Testing max values
        """
        r, g, b = (255, 255, 255)
        res = rgb(r, g, b)
        self.assertEqual(res, "FFFFFF")

    def test_4(self):
        """
        Testing near max values
        """
        r, g, b = (254, 253, 252)
        res = rgb(r, g, b)
        self.assertEqual(res, "FEFDFC")

    def test_5(self):
        """
        Testing our of range values
        """
        r, g, b = (-20, 275, 125)
        res = rgb(r, g, b)
        self.assertEqual(res, "00FF7D")


if __name__ == "__main__":
    unittest.main()
