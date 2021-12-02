# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits
# in descending order.
# Essentially, rearrange the digits to create the highest possible number.
# Examples:
# Input: 42145 Output: 54421
# Input: 145263 Output: 654321
# Input: 123456789 Output: 987654321

def descending_order(num):
    int_list = list(str(num))
    int_list.sort(reverse=True)
    join_int = ''.join(int_list)
    return int(join_int)


print(descending_order(145263))