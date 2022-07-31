"""
The Fibonacci sequence is traditionally used to explain tree recursion.

def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

This algorithm serves welll its educative purpose but it's tremendously inefficient,
not only because of recursion, but because we invoke the fibonacci function twice,
and the right branch of recursion (i.e. fibonacci(n-2)) recalculates all the Fibonacci numbers
already calculated by the left branch (i.e. fibonacci(n-1)).

This algorithm is so inefficient that the time to calculate any Fibonacci number over 50
is simply too much.You may go for a cup of coffee or go take a nap while you wait for the answer.
But if you try it here in Code Wars you will most likely get a code timeout before any answers.

For this particular Kata we want to implement the memoization solution.
This will be cool because it will let us keep using the tree recursion algorithm while still
keeping itsufficiently optimized to get an answer very rapidly.

The trick of the memoized version is that we will keep a cache data structure
(most likely an associative array) where we will store the Fibonacci numbers as we calculate them.
When a Fibonacci number is calculated, we first look it up in the cache, if it's not there,
we calculate it and put it in the cache, otherwise we returned the cached number.

Refactor the function into a recursive Fibonacci function that using a memoized data structure
avoids the deficiencies of tree recursion.
Can you make it so the memoization cache is private to this function?
"""
import unittest
import functools

import timeout_decorator

GLOBAL_TIMEOUT = 1


@functools.lru_cache(None)
def fibonacci(number: int) -> int:
    """
    Calculate fibonacci sequence recursively
    """
    if number in [0, 1]:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


class MemoizedFibonacciTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test_1(self):
        """
        Test 1
        """
        test = 50
        res = fibonacci(test)
        self.assertEqual(res, 12586269025)

        # test argument mutation
        self.assertEqual(test, 50)

    def test_2(self):
        """
        Test 2
        """
        test = 60
        res = fibonacci(test)
        self.assertEqual(res, 1548008755920)

        # test argument mutation
        self.assertEqual(test, 60)

    def test_3(self):
        """
        Test 3
        """
        test = 70
        res = fibonacci(test)
        self.assertEqual(res, 190392490709135)

        # test argument mutation
        self.assertEqual(test, 70)


if __name__ == "__main__":
    timeout_decorator.timeout(GLOBAL_TIMEOUT)(unittest.main)()
