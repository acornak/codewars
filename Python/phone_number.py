# Write a function that accepts an array of 10 integers 
# (between 0 and 9), that returns a string of those numbers 
# in the form of a phone number.
# Example: create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parentheses!
import unittest


def create_phone_number(n):
    if len(n) != 10:
        raise Exception("Invalid input")

    for number in n:
        if len(str(number)) > 1:
            raise Exception("Only 1 digit numbers allowed")
        try: 
            int(number)
        except ValueError:
            raise Exception("Array should only contain numbers")

    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


class PhoneNumberTestCase(unittest.TestCase):
    def test_invalid_array_1(self):
        test_case = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]

        with self.assertRaises(Exception) as context:
            create_phone_number(test_case)

        self.assertTrue("Invalid input" in str(context.exception))
    
    def test_invalid_array_2(self):
        test_case = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        with self.assertRaises(Exception) as context:
            create_phone_number(test_case)

        self.assertTrue("Invalid input" in str(context.exception))

    def test_invalid_array_3(self):
        test_case = [1, 2, 3, 4, 5, 6, 7, 8, 9, "a"]

        with self.assertRaises(Exception) as context:
            create_phone_number(test_case)

        self.assertTrue("Array should only contain numbers" in str(context.exception))

    def test_invalid_array_4(self):
        test_case = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        with self.assertRaises(Exception) as context:
            create_phone_number(test_case)

        self.assertTrue("Only 1 digit numbers allowed" in str(context.exception))

    def test_valid_array_1(self):
        test_case = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

        self.assertTrue("(123) 456-7890", create_phone_number(test_case))

    def test_valid_array_2(self):
        test_case = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        self.assertTrue("(111) 111-1111", create_phone_number(test_case))

    def test_valid_array_3(self):
        test_case = [0, 2, 3, 0, 5, 6, 0, 8, 9, 0]

        self.assertTrue("(023) 056-0890", create_phone_number(test_case))

    def test_valid_array_4(self):
        test_case = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.assertTrue("(000) 000-0000", create_phone_number(test_case))

    def test_valid_array_5(self):
        test_case = [1, "2", 3, 4, 5, 6, 7, 8, 9, 0]

        self.assertTrue("(123) 456-7890", create_phone_number(test_case))


if __name__ == "__main__":
    unittest.main()
