# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more
# letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.
#
# Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns
# "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"
test_1 = "Hey fellow warriors"
test_2 = "This is a test"
test_3 = "This is another test"


def spinWords(sentence: str) -> str:
    listed = sentence.split(' ')
    result = []
    for x in listed:
        if len(x) > 5:
            temp = []
            for character in range(len(x) - 1, -1, -1):
                temp.append(x[character])
            result.append(''.join(temp))
        else:
            result.append(x)
    return ' '.join(result)


def spin_words(sentence: str) -> str:
    return ' '.join([''.join([x[character] for character in range(len(x) - 1, -1, -1)]) if len(x) > 4 else x for x in sentence.split(' ')])


print(spinWords(test_1))
