# Your job is to write a function which increments a string, to create a new string.
#
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:
#
# foo -> foo1
#
# foobar23 -> foobar24
#
# foo0042 -> foo0043
#
# foo9 -> foo10
#
# foo099 -> foo100
# !J_~39578Sqw413888032@9"mFTu=723274516:cpthxek38iGxwB155ar500003069
# Attention: If the number has leading zeros the amount of digits should be considered.
text = '!J_~39578Sqw413888032@9"mFTu=723274516:cpthxek38iGxwB155ar500003069'


def increment_string(message):
    import re
    digit_part = re.compile(r'[a-zA-z]*(?P<digit>[0-9]*)$')
    last_number = digit_part.search(message).group('digit')
    print(last_number)
    if last_number == '':
        return message + '1'
    else:
        character = message[:-len(last_number)]
        digit_plus_one = int(last_number) + 1
        zero_trail = len(last_number)
        return f'{character}{digit_plus_one:0{zero_trail}}'


print(increment_string(text))
