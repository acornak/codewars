# pylint: disable=invalid-name
"""
The numbers 6, 12, 18, 24, 36, 48 have a common property.
They have the same two prime factors that are 2 and 3.

If we see their prime factorization we will see it more clearly:

6 = 2 * 3
12 = 2^2 * 3
18 = 2 * 3^2
24 = 2^3 * 3
36 = 2^2 * 3^2
48 = 2^4 * 3
48 is the maximum of them bellow the value 50

We may see another cases, for numbers that have another two prime factors like: 5, 11,
but bellow (or equal) a maximum value 1000

55 = 5 * 11
275 = 5^2 * 11
605 = 5 * 11^2
In this case 605 is the highest possible number bellow 1000.

Make the function highest_biPrimefac(), that receives two primes as arguments and a maximum limit,
nMax(found numbers should be less or equal to nMax). Output should be a list or array of highest
number found and the corresponding exponents of primes in order given.
Representing the features for this function:

highest_biPrimefac(p1, p2, nMax) -------> [max.number, k1, k2]

max.number = p1^k1 * p2^k2 <= nMax

p1 < p2 and k1 >= 1, k2 >= 1
Let's see the cases we have above:

highest_biPrimefac(2, 3, 50) ------> [48, 4, 1]

highest_biPrime(5, 11, 1000) ------> [605, 1, 2]
Enjoy it and happy coding!

https://www.codewars.com/kata/55f347cfb44b879e1e00000d/python
"""

import unittest


def highest_biPrimefac(p1: int, p2: int, n: int) -> list[int]:
    """
    Returns highest number
    """
    res = []
    i = 1
    j = 1

    while p1**i <= n / p2:
        i += 1

    while p2**j <= n / p1:
        j += 1

    for k in range(1, i):
        for l in range(1, j):
            if p1**k * p2**l <= n:
                res.append([p1**k * p2**l, k, l])
    return max(res)


class DuplicateEncoderTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test_1(self):
        """
        Test 1
        """
        p1 = 2
        p2 = 3
        n = 50
        res = highest_biPrimefac(p1, p2, n)
        self.assertEqual(res, [48, 4, 1])

    def test_2(self):
        """
        Test 2
        """
        p1 = 5
        p2 = 11
        n = 1000
        res = highest_biPrimefac(p1, p2, n)
        self.assertEqual(res, [605, 1, 2])

    def test_3(self):
        """
        Test 3
        """
        p1 = 3
        p2 = 13
        n = 5000
        res = highest_biPrimefac(p1, p2, n)
        self.assertEqual(res, [4563, 3, 2])

    def test_4(self):
        """
        Test 4
        """
        p1 = 5
        p2 = 7
        n = 5000
        res = highest_biPrimefac(p1, p2, n)
        self.assertEqual(res, [4375, 4, 1])


if __name__ == "__main__":
    unittest.main()
