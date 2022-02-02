# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other
# elements.
#
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
import unittest


def move_zeros(array):
    result = []
    zero_count = 0
    for number in array:
        if number != 0:
            result.append(number)
        else:
            zero_count += 1
    for zero in range(zero_count):
        result.append(0)
    return result


class MyTestCase(unittest.TestCase):
    def test_basic_return(self):
        self.assertEqual(move_zeros([1, 0, 1, 2, 0, 1, 3]), [1, 1, 2, 1, 3, 0, 0])  # add assertion here
        self.assertEqual(move_zeros(
            [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
            [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_only_zeros(self):
        self.assertEqual(move_zeros([0, 0]), [0, 0])

    def test_empty(self):
        self.assertEqual(move_zeros([]), [])


if __name__ == '__main__':
    unittest.main(verbosity=2)

