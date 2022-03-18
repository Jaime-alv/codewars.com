# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The
# function should return true if the string is valid, and false if it's invalid.
#
# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
# Constraints
# 0 <= input.length <= 100
#
# Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the
# input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as
# parentheses (e.g. [], {}, <>).
import unittest


def valid_parentheses(word):
    if word.count('(') != word.count(')'):
        return False
    else:
        temp = []
        for character in word:
            if character == '(':
                temp.append('(')
            elif character == ')' and len(temp) > 0:
                temp.pop()
        if len(temp) == 0:
            return True
        else:
            return False


def other_solution(word):
    cnt = 0
    for char in word:
        if char == '(':
            cnt += 1
        if char == ')':
            cnt -= 1
        if cnt < 0:
            return False
    return True if cnt == 0 else False


class TestCases(unittest.TestCase):
    def test_true(self):
        self.assertTrue(valid_parentheses("()"))
        self.assertTrue(valid_parentheses("(())((()())())"))
        self.assertTrue(valid_parentheses("(at#s[sle)"))
        self.assertTrue(valid_parentheses(""))

    def test_false(self):
        self.assertFalse(valid_parentheses('('))
        self.assertFalse(valid_parentheses(")(()))"))

    def test_hard_order(self):
        self.assertFalse(valid_parentheses(")("))
        self.assertFalse(valid_parentheses("hi())("))
        self.assertTrue(valid_parentheses("hi(hi)()"))


if __name__ == '__main__':
    unittest.main(verbosity=2)
