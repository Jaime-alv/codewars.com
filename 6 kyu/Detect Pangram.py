# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence
# "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once
# (case is irrelevant).
#
# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and
# punctuation.
test = "The quick brown fox jumps over the lazy dog"
import string


def is_pangram(s):
    abc = string.ascii_lowercase
    abc_dict = {}
    for letter in abc:
        abc_dict.setdefault(letter, 0)
    for character in s:
        if character.lower() in abc_dict:
            abc_dict[character.lower()] += 1
    for counting in abc_dict:
        if abc_dict[counting] == 0:
            return False
    return True


def pangram(s):
    for character in string.ascii_lowercase:
        if character not in s.lower():
            return False
    return True


print(pangram(test))
