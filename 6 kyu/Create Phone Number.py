# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the
# form of a phone number.
#
# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parentheses!

import unittest


def create_phone_number(array):
    return f"({array[0]}{array[1]}{array[2]}) {array[3]}{array[4]}{array[5]}-{array[6]}{array[7]}{array[8]}{array[9]}"


def codewars(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)  # *n == unpack n


class TestCase(unittest.TestCase):
    def test_base(self):
        self.assertEqual(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
        self.assertEqual(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
        self.assertEqual(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
        self.assertEqual(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")

    def length(self):
        self.assertFalse(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9]))
        self.assertTrue(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


if __name__ == '__main__':
    unittest.main(verbosity=2)
