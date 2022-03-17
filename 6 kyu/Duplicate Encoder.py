# The goal of this exercise is to convert a string to a new string where each character in the new string is "("
# if that character appears only once in the original string, or ")" if that character appears more than once in the
# original string. Ignore capitalization when determining if a character is a duplicate.
#
# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("
# Notes
# Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX",
# the "XXX" is the expected result, not the input!
import unittest


def duplicate_encode2(string: str):
    result = []
    for element in string:
        if string.lower().count(element.lower()) == 1:
            result.append('(')
        else:
            result.append(')')
    return ''.join(result)


def duplicate_encode(string):
    return ''.join(['(' if string.lower().count(element.lower()) == 1 else ')' for element in string])


class TestCase(unittest.TestCase):

    def test_din(self):
        self.assertEqual(duplicate_encode('din'), '(((')

    def test_basic(self):
        self.assertEqual(duplicate_encode("recede"), "()()()")
        self.assertEqual(duplicate_encode("Success"), ")())())")
        self.assertEqual(duplicate_encode("(( @"), "))((")

    def test_random(self):
        self.assertEqual(duplicate_encode("SNLpefjbTn!p)E!SoSrWQqkBfQVu !J"), '))()))))()))()))()(())()))((())')
        self.assertEqual(duplicate_encode("mwFSKhRZ liqLQBZLoagrOerqgTqKh@"), '(((())))()()))()))()))()))()))(')


if __name__ == '__main__':
    unittest.main()
