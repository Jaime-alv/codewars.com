# Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. Since James
# doesn't know how to make this happen, he needs your help.
#
# Task
# You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters.
# Trailing spaces should be removed, and every line must be terminated with a newline character (\n).
#
# Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even
# or negative size.
#
# Examples
# A size 3 diamond:
#
#  *
# ***
#  *
# ...which would appear as a string of " *\n***\n *\n"
#
# A size 5 diamond:
#
# 11*11 == 5
# 1***1 == 5
# ***** == 5
# 1***
# 11*
# ...that is:
#
# "  *\n ***\n*****\n ***\n  *\n"

def diamond(number):
    if number % 2 == 0 or number < 0:
        return None
    else:
        shape = [n for n in range(1, number + 1, 2)]
        space = [y for y in range(number // 2, -1, -1)]
        result = []
        for index in range(len(shape)):
            result.append(' ' * space[index] + '*' * shape[index] + '\n')
        for index in range(len(shape) - 2, -1, -1):
            result.append(' ' * space[index] + '*' * shape[index] + '\n')
        endpoint = ''.join(result)
        return endpoint


print(diamond(15))

def zip_mode(number):
    result = []
    shape = [n for n in range(1, number + 1, 2)]
    space = [y for y in range(number // 2, -1, -1)]
    for index in range(len(shape)):
        result.append(' ' * space[index] + '*' * shape[index] + '\n')
    for index in range(len(shape) - 2, -1, -1):
        result.append(' ' * space[index] + '*' * shape[index] + '\n')
    endpoint = ''.join(result)