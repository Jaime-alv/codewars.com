# The Fibonacci numbers are the numbers in the following integer sequence (Fn):
#
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...
#
# such as
#
# F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.
#
# Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying
#
# F(n) * F(n+1) = prod.
#
# Your function productFib takes an integer (prod) and returns an array:
#
# [F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
# depending on the language if F(n) * F(n+1) = prod.
#
# If you don't find two consecutive F(n) verifying F(n) * F(n+1) = prod you will return
#
# [F(n), F(n+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
# F(n) being the smallest one such as F(n) * F(n+1) > prod.
#
# Some Examples of Return:
# (depend on the language)
#
# productFib(714) # should return (21, 34, true),
#                 # since F(8) = 21, F(9) = 34 and 714 = 21 * 34
#
# productFib(800) # should return (34, 55, false),
#                 # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
# -----
# productFib(714) # should return [21, 34, true],
# productFib(800) # should return [34, 55, false],
# -----
# productFib(714) # should return {21, 34, 1},
# productFib(800) # should return {34, 55, 0},
# -----
# productFib(714) # should return {21, 34, true},
# productFib(800) # should return {34, 55, false},
# Note:
# You can see examples for your language in "Sample Tests".
import unittest


def productFib(prod):
    result = []
    fib_series = fibonacci(1000)
    for index in range(len(fib_series) - 1):
        if fib_series[index] * fib_series[index + 1] == prod:
            result.append(fib_series[index])
            result.append(fib_series[index + 1])
            result.append(True)
            break
        if fib_series[index] * fib_series[index + 1] > prod:
            result.append(fib_series[index])
            result.append(fib_series[index + 1])
            result.append(False)
            break
    return result


def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    else:
        count = 2
        result = [0, 1]
        while count < n:
            temp = result[-1] + result[-2]
            result.append(temp)
            count += 1
        return result


def clean_productFib(prod):
    a, b = 0, 1
    while prod > a * b:
        a, b = b, a + b
    return [a, b, prod == a * b]


class TestCase(unittest.TestCase):
    def test_Fibonacci(self):
        self.assertEqual(fibonacci(0), [])
        self.assertEqual(fibonacci(1), [0])
        self.assertEqual(fibonacci(2), [0, 1])
        self.assertEqual(fibonacci(3), [0, 1, 1])
        self.assertEqual(fibonacci(4), [0, 1, 1, 2])
        self.assertEqual(fibonacci(8), [0, 1, 1, 2, 3, 5, 8, 13])

    def test_product(self):
        self.assertEqual(productFib(714), [21, 34, True])
        self.assertEqual(productFib(800), [34, 55, False])

    def test_basic_codewars(self):
        self.assertEqual(productFib(4895), [55, 89, True])
        self.assertEqual(productFib(5895), [89, 144, False])


if __name__ == '__main__':
    unittest.main(verbosity=2)
