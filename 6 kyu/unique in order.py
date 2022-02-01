# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any
# elements with the same value next to each other and preserving the original order of elements.
#
# For example:
#
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]
import unittest


def unique_in_order(iterable):
    result = []
    if len(iterable) > 0:
        if len(iterable) == 1:
            result.append(iterable[0])
        elif iterable.count(iterable[0]) == len(iterable):
            result.append(iterable[0])
        else:
            for index in range(len(iterable)):
                if iterable[index] != iterable[index - 1]:
                    result.append(iterable[index])
    return result


class MyTestCase(unittest.TestCase):
    def test_function(self):
        self.assertEqual(unique_in_order('AAAABBBCCDAABBB'), ['A', 'B', 'C', 'D', 'A', 'B'])
        self.assertEqual(unique_in_order('A'), ['A'])
        self.assertEqual(unique_in_order('ABBCcAD'), ['A', 'B', 'C', 'c', 'A', 'D'])

    def test_duplicates(self):
        self.assertEqual(unique_in_order('AAAAAAAAAA'), ['A'])

    def test_digits(self):
        self.assertEqual(unique_in_order([1, 2, 2, 3, 3]), [1, 2, 3])

    def test_empty(self):
        self.assertEqual(unique_in_order(''), [])


if __name__ == '__main__':
    unittest.main(verbosity=1)
