# You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to
# an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a
# Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings
# representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter
# (direction) and you know it takes you one minute to traverse one city block, so create a function that will return
# true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will,
# of course, return you to your starting point. Return false otherwise.
#
# Note: you will always receive a valid array (string in COBOL) containing a random assortment of direction letters
# ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).

import unittest


def is_valid_walk(array):
    position = {'x': 0, 'y': 0}
    if len(array) == 10:
        for direction in array:
            if direction == 'n':
                position['y'] += 1
            elif direction == 's':
                position['y'] -= 1
            elif direction == 'w':
                position['x'] += 1
            elif direction == 'e':
                position['x'] -= 1
        if position['x'] == 0 and position['y'] == 0:
            return True
        else:
            return False
    else:
        return False


def one_liner(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')


class TestCase(unittest.TestCase):
    def test_array_length(self):
        self.assertFalse(is_valid_walk([1, 2, 4]))
        self.assertTrue(is_valid_walk([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    def test_base_case(self):
        self.assertTrue(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))
        self.assertFalse(is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']))
        self.assertFalse(is_valid_walk(['w']))
        self.assertFalse(is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))

    def test_complex(self):
        self.assertFalse(is_valid_walk(['e', 'w', 'e', 'w', 'n', 'n', 'n', 's', 'e', 'w']))


if __name__ == '__main__':
    unittest.main(verbosity=2)
