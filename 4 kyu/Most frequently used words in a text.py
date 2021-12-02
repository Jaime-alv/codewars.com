# Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the
# top-3 most occurring words, in descending order of the number of occurrences.
#
# Assumptions:
# A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
# Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
# Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
# Matches should be case-insensitive, and the words in the result should be lowercased.
# Ties may be broken arbitrarily.
# If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty
# array if a text contains no words.
# Examples:
# top_3_words("In a village of La Mancha, the name of which I have no desire to call to
# mind, there lived not long since one of those gentlemen that keep a lance
# in the lance-rack, an old buckler, a lean hack, and a greyhound for
# coursing. An olla of rather more beef than mutton, a salad on most
# nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
# on Sundays, made away with three-quarters of his income.")
# # => ["a", "of", "on"]
#
# top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# # => ["e", "ddd", "aa"]
#
# top_3_words("  //wont won't won't")
# # => ["won't", "wont"]
# Bonus points (not really, but just for fun):
# Avoid creating an array whose memory footprint is roughly as big as the input text.
# Avoid sorting the entire array of unique words.
quijote = "In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since " \
          "one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound " \
          "for coursing. An olla of rather more beef than mutton, a salad on most nights, scraps on Saturdays, " \
          "lentils on Fridays, and a pigeon or so extra on Sundays, made away with three-quarters of his income. "
randm = "e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"

import re

word_used = {}
most_used = []
most_times = 0
second_word = 0
third_word = 0
word = re.compile(r'(\'*\w+\'?\w*\'*)', re.IGNORECASE)
mo = word.findall(randm)
for words in mo:
    word_used.setdefault(words, 0)
    word_used[words] += 1
for first in word_used:
    if word_used[first] > most_times:
        most_times = word_used[first]
for first in word_used:
    if word_used[first] == most_times:
        most_used.append(first)
for second in word_used:
    if second_word < word_used[second] < most_times:
        second_word = word_used[second]
for second in word_used:
    if word_used[second] == second_word:
        most_used.append(second)
for third in word_used:
    if third_word < word_used[third] < second_word:
        third_word = word_used[third]
for third in word_used:
    if word_used[third] == third_word:
        most_used.append(third)
print(most_used)
