# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
# IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.
#
# Valid inputs examples:
# Examples of valid inputs:
# 1.2.3.4
# 123.45.67.89
# Invalid input examples:
# 1.2.3
# 1.2.3.4.5
# 123.456.78.90
# 123.045.067.089
# Notes:
# Leading zeros (e.g. 01.02.03.04) are considered invalid
# Inputs are guaranteed to be a single string
enter = '123.045.067.089'
valid = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
accepted = ['1234567890.']
ex = '123.456.789.0'  # False


def is_valid_IP(strng):
    return len([x for x in strng.split('.') if x.isdigit() and 0 <= int(x) <= 255 and len(x) == len(str(int(x)))]) == 4


print(is_valid_IP('123.45.67.89'))
