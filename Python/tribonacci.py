"""
Well met with Fibonacci bigger brother, AKA Tribonacci.

As the name may already reveal, it works basically like a Fibonacci,
but summing the last 3 (instead of 2) numbers of the sequence to generate the next.

So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature),
we have this sequence:

[1, 1 ,1, 3, 5, 9, 17, 31, ...]

But what if we started with [0, 0, 1] as a signature?
As starting with [0, 1] instead of [1, 1] basically shifts the common Fibonacci sequence
by once place, you may be tempted to think that we would get the same sequence shifted by 2 places,
but that is not the case and we would get:

[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]

Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function
that given a signature array/list, returns the first n elements
signature included of the so seeded sequence.

Signature will always contain 3 numbers; n will always be a non-negative number;
if n == 0, then return an empty array and be ready for anything else
which is not clearly specified ;)
"""
import unittest


def tribonacci(signature: list[int, float], number: int) -> list[int, float]:
    """
    Tribonacci sequence
    """
    if len(signature) != 3 or number < 0:
        raise Exception("Invalid arguments")

    if number == 0:
        return []

    if number < 3:
        return signature[:number]

    res = signature.copy()
    for _ in range(number - 3):
        res.append(sum(res[-3:]))

    return res


class TribonacciTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test_1(self):
        """
        Test 1
        """
        signature = [1, 1, 1]
        number = 10
        res = tribonacci(signature, number)
        self.assertEqual(res, [1, 1, 1, 3, 5, 9, 17, 31, 57, 105])

        # test argument mutation
        self.assertEqual(signature, [1, 1, 1])
        self.assertEqual(number, 10)

    def test_2(self):
        """
        Test 2
        """
        signature = [0, 0, 1]
        number = 10
        res = tribonacci(signature, number)
        self.assertEqual(res, [0, 0, 1, 1, 2, 4, 7, 13, 24, 44])

        # test argument mutation
        self.assertEqual(signature, [0, 0, 1])
        self.assertEqual(number, 10)

    def test_3(self):
        """
        Test 3
        """
        signature = [0, 1, 1]
        number = 10
        res = tribonacci(signature, number)
        self.assertEqual(res, [0, 1, 1, 2, 4, 7, 13, 24, 44, 81])

        # test argument mutation
        self.assertEqual(signature, [0, 1, 1])
        self.assertEqual(number, 10)

    def test_4(self):
        """
        Test 4
        """
        signature = [1, 0, 0]
        number = 10
        res = tribonacci(signature, number)
        self.assertEqual(res, [1, 0, 0, 1, 1, 2, 4, 7, 13, 24])

        # test argument mutation
        self.assertEqual(signature, [1, 0, 0])
        self.assertEqual(number, 10)

    def test_5(self):
        """
        Test 5
        """
        signature = [0, 0, 0]
        number = 10
        res = tribonacci(signature, number)
        self.assertEqual(res, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        # test argument mutation
        self.assertEqual(signature, [0, 0, 0])
        self.assertEqual(number, 10)

    def test_6(self):
        """
        Test 6
        """
        signature = [1, 2, 3]
        number = 10
        res = tribonacci(signature, number)
        self.assertEqual(res, [1, 2, 3, 6, 11, 20, 37, 68, 125, 230])

        # test argument mutation
        self.assertEqual(signature, [1, 2, 3])
        self.assertEqual(number, 10)

    def test_7(self):
        """
        Test 7
        """
        signature = [3, 2, 1]
        number = 10
        res = tribonacci(signature, number)
        self.assertEqual(res, [3, 2, 1, 6, 9, 16, 31, 56, 103, 190])

        # test argument mutation
        self.assertEqual(signature, [3, 2, 1])
        self.assertEqual(number, 10)

    def test_8(self):
        """
        Test 8
        """
        signature = [1, 1, 1]
        number = 1
        res = tribonacci(signature, number)
        self.assertEqual(res, [1])

        # test argument mutation
        self.assertEqual(signature, [1, 1, 1])
        self.assertEqual(number, 1)

    def test_9(self):
        """
        Test 9
        """
        signature = [0.5, 0.5, 0.5]
        number = 30
        res = tribonacci(signature, number)
        self.assertEqual(
            res,
            [
                0.5,
                0.5,
                0.5,
                1.5,
                2.5,
                4.5,
                8.5,
                15.5,
                28.5,
                52.5,
                96.5,
                177.5,
                326.5,
                600.5,
                1104.5,
                2031.5,
                3736.5,
                6872.5,
                12640.5,
                23249.5,
                42762.5,
                78652.5,
                144664.5,
                266079.5,
                489396.5,
                900140.5,
                1655616.5,
                3045153.5,
                5600910.5,
                10301680.5,
            ],
        )

        # test argument mutation
        self.assertEqual(signature, [0.5, 0.5, 0.5])
        self.assertEqual(number, 30)


if __name__ == "__main__":
    unittest.main()
