"""
This kata aims to show the vulnerabilities of hashing functions for short messages.

When provided with a SHA-256 hash, return the value that was hashed.
You are also given the characters that make the expected value, but in alphabetical order.

The returned value is less than 10 characters long. Return nil for Ruby and Crystal,None for
Python,null for for Java and Javascript when the hash cannot be cracked with the given characters.

Example:
Example arguments: '5694d08a2e53ffcae0c3103e5ad6f6076abd960eb1f8a56577040bc1028f702b', 'cdeo'
Correct output: 'code'
"""
import hashlib
from itertools import permutations

import unittest


def sha256_cracker(hash_str: str, chars: str) -> str:
    """
    SHA 256 Cracker
    """
    for combination in permutations(chars, len(chars)):
        combination = "".join(combination)
        if hashlib.sha256(str.encode(combination)).hexdigest() == hash_str:
            return combination

    return None


class SHACrackerTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test_1(self):
        """
        Test 1
        """
        hash_str = "b8c49d81cb795985c007d78379e98613a4dfc824381be472238dbd2f974e37ae"
        encoded = "deGioOstu"
        res = sha256_cracker(hash_str, encoded)
        self.assertEqual(res, "GoOutside")

        # test argument mutation
        self.assertEqual(
            hash_str, "b8c49d81cb795985c007d78379e98613a4dfc824381be472238dbd2f974e37ae"
        )
        self.assertEqual(encoded, "deGioOstu")


if __name__ == "__main__":
    # unittest.main()
    print(
        sha256_cracker(
            "b8c49d81cb795985c007d78379e98613a4dfc824381be472238dbd2f974e37ae",
            "deGioOstu",
        )
    )
