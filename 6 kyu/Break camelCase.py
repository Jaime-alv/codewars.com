# Complete the solution so that the function will break up camel casing, using a space between words.
#
# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""
import string

test3 = 'breakCamelCase'
test = 'camelCasing'
test4 = 'leaveTakeAskSeeFew'


def solution(s):
    upper = string.ascii_uppercase
    for x in upper:
        s = s.replace(x, ' ' + x)
    return s


def solution2(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)


print(solution(test4))
