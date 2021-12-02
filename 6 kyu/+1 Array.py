# Given an array of integers of any length, return an array that has 1 added to the value represented by the array.
#
# the array can't be empty
# only non-negative, single digit integers are allowed
# Return nil (or your language's equivalent) for invalid inputs.
#
# Examples
# For example the array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].
#
# [4, 3, 2, 5] would return [4, 3, 2, 6]

def arrayplusone(array):
    appendix = [str(n) for n in array]
    join_appendix = ''.join(appendix)
    join_appendix = int(join_appendix) + 1
    solution = list(str(join_appendix))
    redone = [int(x) for x in solution]
    print(redone)


text1 = [4, 3, 2, 5]
text2 = [2, 3, 9]
text3 = ['Hello']
text4 = [1, -2, 3, 4]


def up_array(arr):
    if len(arr) == 0:
        return None
    for x in arr:
        if not 0 <= x <= 9:
            return None
    return [int(x) for x in list(str(int(''.join([str(n) for n in arr])) + 1))]


def up_array_pretty(arr):
    return None if [x for x in arr if not 0 <= x <= 9] or arr == [] else [int(x) for x in list(
        str(int(''.join([str(n) for n in arr])) + 1))]


print(up_array(text4))
