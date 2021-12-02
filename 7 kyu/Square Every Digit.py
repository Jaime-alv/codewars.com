# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
#
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
#
# Note: The function accepts an integer and returns an integer


def square_digits(num):
    number_str = str(num)
    junts = []
    for y in number_str:
        y = int(y) ** 2
        junts.append(str(y))
    junts = ''.join(junts)
    return int(junts)


print(square_digits(9119))