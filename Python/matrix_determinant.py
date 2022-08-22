# pylint: disable=invalid-name
"""
Write a function that accepts a square matrix (N x N 2D array)
and returns the determinant of the matrix.

How to take the determinant of a matrix -- it is simplest to start with the smallest cases:

A 1x1 matrix |a| has determinant a.

A 2x2 matrix [ [a, b], [c, d] ] or

|a  b|
|c  d|
has determinant: a*d - b*c.

The determinant of an n x n sized matrix is calculated by
reducing the problem to the calculation of the determinants of n matrices ofn-1 x n-1 size.

For the 3x3 case, [ [a, b, c], [d, e, f], [g, h, i] ] or

|a b c|
|d e f|
|g h i|
the determinant is: a * det(a_minor) - b * det(b_minor) + c * det(c_minor)
where det(a_minor) refers to taking the determinant of the 2x2 matrix
created by crossing out the row and column in which the element a occurs:

|- - -|
|- e f|
|- h i|
Note the alternation of signs.

The determinant of larger matrices are calculated analogously,
e.g. if M is a 4x4 matrix with first row [a, b, c, d], then:

det(M) = a * det(a_minor) - b * det(b_minor) + c * det(c_minor) - d * det(d_minor)

https://www.codewars.com/kata/52a382ee44408cea2500074c
"""
import unittest


class Matrix:
    """
    Matrix class
    """

    def __init__(self, matrix: list[list[int]]) -> None:
        """
        Constructor
        """
        self.__matrix: list[list[int]] = matrix
        self.__result: int = 0

    def __validate_matrix(self) -> None:
        """
        Validate whether the matrix is square
        """
        for elem in self.__matrix:
            if len(elem) != len(self.__matrix):
                raise ValueError("invalid matrix format")

    def __create_sub_matrix(self, i: int, matrix: list[list[int]]) -> list[list[int]]:
        """
        Remove first row from matrix and i-th element from each row
        """
        res = []

        for j in range(1, len(matrix)):
            res.append(matrix[j][:i] + matrix[j][i + 1 :])
        return res

    def __recursive_get_determinant(
        self, matrix: list[list[int]], factor: int = 1
    ) -> None:
        """
        Recursively create matrices until 2x2
        """
        if len(matrix) == 2:
            self.__result += factor * (
                matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            )
            return

        for i in range(len(matrix)):
            new_matrix = self.__create_sub_matrix(i, matrix)
            self.__recursive_get_determinant(new_matrix)

    def get_determinant(self) -> int:
        """
        Calculate determinant of a matrix
        """
        self.__validate_matrix()

        if len(self.__matrix) == 1:
            return self.__matrix[0][0]

        self.__recursive_get_determinant(self.__matrix)

        return self.__result


def determinant(matrix: list[list[int]]) -> int:
    """
    Returns determinant of a matrix
    """
    return Matrix(matrix).get_determinant()


class MatrixTestCase(unittest.TestCase):
    """
    Unit tests
    """

    def test_1(self):
        """
        Test 1x1 matrix
        """
        test_case = [[5]]
        res = determinant(test_case)
        self.assertEqual(res, 5)

        # test argument mutation
        self.assertTrue(test_case, [[5]])

    def test_2(self):
        """
        Test 2x2 matrix
        """
        test_case = [
            [4, 6],
            [3, 8],
        ]
        res = determinant(test_case)
        self.assertEqual(res, 14)

        # test argument mutation
        self.assertTrue(test_case, [[4, 6], [3, 8]])

    def test_3(self):
        """
        Test 3x3 matrix
        """
        test_case = [
            [2, 4, 2],
            [3, 1, 1],
            [1, 2, 0],
        ]
        res = determinant(test_case)
        self.assertEqual(res, 10)

        # test argument mutation
        self.assertTrue(test_case, [[2, 4, 2], [3, 1, 1], [1, 2, 0]])

    def test_4(self):
        """
        Test 4x4 matrix
        """
        test_case = [
            [1, 2, 3, 4],
            [5, 0, 2, 8],
            [3, 5, 6, 7],
            [2, 5, 3, 1],
        ]
        res = determinant(test_case)
        self.assertEqual(res, 24)

        # test argument mutation
        self.assertTrue(
            test_case, [[1, 2, 3, 4], [5, 0, 2, 8], [3, 5, 6, 7], [2, 5, 3, 1]]
        )

    def test_5(self):
        """
        Test 5x5 matrix
        """
        test_case = [
            [2, 5, 3, 6, 3],
            [17, 5, 7, 4, 2],
            [7, 8, 5, 3, 2],
            [9, 4, -6, 8, 3],
            [2, -5, 7, 4, 2],
        ]
        res = determinant(test_case)
        self.assertEqual(res, 2060)

        # test argument mutation
        self.assertTrue(
            test_case,
            [
                [2, 5, 3, 6, 3],
                [17, 5, 7, 4, 2],
                [7, 8, 5, 3, 2],
                [9, 4, -6, 8, 3],
                [2, -5, 7, 4, 2],
            ],
        )

    def test_6(self):
        """
        Test 8x8 matrix
        """
        test_case = [
            [10, -10, -5, 7, -4, -4, 3, 3],
            [-5, -10, 5, 9, -2, 2, 8, 6],
            [6, 4, 2, -2, 9, -2, -7, -7],
            [-6, 0, 2, 8, -1, 3, -6, 2],
            [-8, -7, 10, -7, -9, 6, 1, -2],
            [2, -7, 0, -4, -1, -6, -6, 9],
            [8, -5, 6, 7, 5, 2, -8, -1],
            [3, -4, 3, 4, 0, -1, -5, 8],
        ]
        res = determinant(test_case)
        self.assertEqual(res, 61360609)

        # test argument mutation
        self.assertTrue(
            test_case,
            [
                [10, -10, -5, 7, -4, -4, 3, 3],
                [-5, -10, 5, 9, -2, 2, 8, 6],
                [6, 4, 2, -2, 9, -2, -7, -7],
                [-6, 0, 2, 8, -1, 3, -6, 2],
                [-8, -7, 10, -7, -9, 6, 1, -2],
                [2, -7, 0, -4, -1, -6, -6, 9],
                [8, -5, 6, 7, 5, 2, -8, -1],
                [3, -4, 3, 4, 0, -1, -5, 8],
            ],
        )

    def test_invalid(self):
        """
        Test invalid matrix format
        """
        test_case = [
            [2, 4, 2],
            [3, 1, 1],
        ]

        with self.assertRaises(ValueError):
            determinant(test_case)

        # test argument mutation
        self.assertTrue(test_case, [[2, 4, 2], [3, 1, 1]])


if __name__ == "__main__":
    unittest.main()
