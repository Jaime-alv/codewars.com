# Complete the function that
#
# accepts two integer arrays of equal length
# compares the value each member in one array to the corresponding member in the other
# squares the absolute value difference between those two values
# and returns the average of those squared absolute value difference between each member pair.
# Examples
# [1, 2, 3], [4, 5, 6]              -->   9   because (9 + 9 + 9) / 3
# [10, 20, 10, 2], [10, 25, 5, -2]  -->  16.5 because (0 + 25 + 25 + 16) / 4
# [-1, 0], [0, -1]                  -->   1   because (1 + 1) / 2
ar1 = [10, 20, 10, 2]
ar2 = [10, 25, 5, -2]


def solution(array1, array2):
    final = [y ** 2 for y in [array1[index] - array2[index] for index in range(len(array1))]]
    return sum(final) / len(final)


print(solution(ar1, ar2))
