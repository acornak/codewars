"""
The Fibonacci numbers are the numbers in the following integer sequence (Fn):

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

such as

F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.

Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying

F(n) * F(n+1) = prod.

Your function productFib takes an integer (prod) and returns an array:

[F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
depending on the language if F(n) * F(n+1) = prod.

If you don't find two consecutive F(n) verifying F(n) * F(n+1) = prodyou will return

[F(n), F(n+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
F(n) being the smallest one such as F(n) * F(n+1) > prod.

Some Examples of Return:
(depend on the language)

productFib(714) # should return [21, 34, true],
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

productFib(800) # should return [34, 55, false],
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
"""
import unittest


def productFib(number: int) -> list[int, bool]:
    """
    Product Fibonacci
    """
    fib = [0, 1]
    while True:
        if fib[-1] * fib[-2] == number:
            return [fib[-2], fib[-1], True]
        if fib[-1] * fib[-2] > number:
            return [fib[-2], fib[-1], False]
        fib.append(fib[-2] + fib[-1])


class ProductFibonacciTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test_1(self):
        """
        Test 1
        """
        self.assertEqual(productFib(714), [21, 34, True])

    def test_2(self):
        """
        Test 2
        """
        self.assertEqual(productFib(800), [34, 55, False])

    def test_3(self):
        """
        Test 3
        """
        self.assertEqual(productFib(5895), [89, 144, False])

    def test_4(self):
        """
        Test 4
        """
        self.assertEqual(productFib(5895), [89, 144, False])

    def test_5(self):
        """
        Test 5
        """
        self.assertEqual(productFib(1), [1, 1, True])

    def test_6(self):
        """
        Test 6
        """
        self.assertEqual(productFib(0), [0, 1, True])


if __name__ == "__main__":
    unittest.main()
