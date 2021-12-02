# Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is
# not repeated anywhere in the string.
#
# For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the
# string, and occurs first in the string.
#
# As an added challenge, upper- and lowercase letters are considered the same character, but the function should return
# the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.
#
# If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.

test = 'sTtreess'


def first_non_repeating_letter(message):
    count = {}
    for character in message.lower():
        count.setdefault(character, 0)
        count[character] += 1
    for letter in count:
        if count[letter] == 1 and letter in message:
            return letter
        elif count[letter] == 1 and letter.capitalize() in message:
            return letter.capitalize()
    return None


print(first_non_repeating_letter(test))
