# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable
# format (HH:MM:SS)
#
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)
#
# You can find some examples in the test fixtures.
import unittest


def make_readable(seconds):
    hour = 0
    minute = 0
    second = 0
    if seconds < 60:
        second = seconds
    if seconds > 59:
        minute += int(seconds / 60)
        second += seconds % 60
    if minute > 59:
        hour += int(minute / 60)
        minute = minute % 60

    return f'{hour:02d}:{minute:02d}:{second:02d}'


def make_readable_easier(seconds):
    h = seconds / 60 ** 2
    m = (seconds % 60 ** 2) / 60
    s = (seconds % 60 ** 2 % 60)
    return "%02d:%02d:%02d" % (h, m, s)


class TestCase(unittest.TestCase):
    def test_seconds(self):
        self.assertEqual(make_readable(50), "00:00:50")
        self.assertEqual(make_readable(90), "00:01:30")
        self.assertEqual(make_readable(60), '00:01:00')

    def test_basic(self):
        self.assertEqual(make_readable(0), '00:00:00')
        self.assertEqual(make_readable(5), '00:00:05')

    def test_hourly(self):
        self.assertEqual(make_readable(86399), "23:59:59")
        self.assertEqual(make_readable(359999), "99:59:59")


if __name__ == '__main__':
    unittest.main(verbosity=2)
