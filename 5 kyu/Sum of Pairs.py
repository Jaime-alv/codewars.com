# Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of
# appearance that add up to form the sum.
#
# sum_pairs([11, 3, 7, 5],         10)
# #              ^--^      3 + 7 = 10
# == [3, 7]
#
# sum_pairs([4, 3, 2, 3, 4],         6)
# #          ^-----^         4 + 2 = 6, indices: 0, 2 *
# #             ^-----^      3 + 3 = 6, indices: 1, 3
# #                ^-----^   2 + 4 = 6, indices: 2, 4
# #  * entire pair is earlier, and therefore is the correct answer
# == [4, 2]
#
# sum_pairs([0, 0, -2, 3], 2)
# #  there are no pairs of values that can be added to produce 2.
# == None/nil/undefined (Based on the language)
#
# sum_pairs([10, 5, 2, 3, 7, 5],         10)
# #              ^-----------^   5 + 5 = 10, indices: 1, 5
# #                    ^--^      3 + 7 = 10, indices: 3, 4 *
# #  * entire pair is earlier, and therefore is the correct answer
# == [3, 7]
# Negative numbers and duplicate numbers can and will appear.
#
# NOTE: There will also be lists tested of lengths upwards of 10,000,000 elements. Be sure your code doesn't time out.
import unittest


def sum_pairs(listed_numbers, total_sum):
    result = []
    for number in listed_numbers:
        if len(result) < 2:
            for addition in listed_numbers:
                if number + addition == total_sum:
                    result.append(number)
                    result.append(addition)
                    break
        else:
            break
    if len(result) == 0:
        return None
    else:
        return result


class TestCases(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(sum_pairs([11, 3, 7, 5], 10), [3, 7])
        self.assertEqual(sum_pairs([4, 3, 2, 3, 4], 6), [4, 2])

    def test_none(self):
        self.assertEqual(sum_pairs([0, 0, -2, 3], 2), None)

    def test_closest(self):
        self.assertEqual(sum_pairs([10, 5, 2, 3, 7, 5], 10), [3, 7])


if __name__ == '__main__':
    unittest.main(verbosity=2)
