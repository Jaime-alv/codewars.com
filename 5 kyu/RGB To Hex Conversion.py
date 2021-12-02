# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
# representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must
# be rounded to the closest valid value.
# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
# Conversion steps:
# Divide the number by 16.
# Get the integer quotient for the next iteration.
# Get the remainder for the hex digit.
# Repeat the steps until the quotient is equal to 0.
# The following are examples of expected output values:
# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3
# 0	0
# 1	1
# 2	2
# 3	3
# 4	4
# 5	5
# 6	6
# 7	7
# 8	8
# 9	9
# 10	A
# 11	B
# 12	C
# 13	D
# 14	E
# 15	F

conversion = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
              13: 'D', 14: 'E', 15: 'F'}
rgb = '148, 0, 211'


def rgb_to_hex(rgb):
    rgb = rgb.split(',')
    result = []
    for x in range(len(rgb)):
        if int(rgb[x]) < 0:
            rgb[x] = 0
        elif int(rgb[x]) > 255:
            rgb[x] = 255
    for y in rgb:
        y = int(y)
        remainder = []
        while y != 0:
            x = y % 16
            remainder.append(x)
            y = int(y / 16)
        if len(remainder) == 2:
            result.append(str(conversion.get(remainder[-1])) + str(conversion.get(remainder[-2])))
        elif len(remainder) == 1:
            result.append('0' + str(conversion.get(remainder[-1])))
        else:
            result.append('00')
    return ''.join(result)


def rgb(r, g, b):
    rgb_list = [r, g, b]
    result = []
    for x in range(len(rgb_list)):
        if int(rgb_list[x]) < 0:
            rgb_list[x] = 0
        elif int(rgb_list[x]) > 255:
            rgb_list[x] = 255
    for y in rgb_list:
        y = int(y)
        remainder = []
        while y != 0:
            x = y % 16
            remainder.append(x)
            y = int(y / 16)
        if len(remainder) == 2:
            result.append(str(conversion.get(remainder[-1])) + str(conversion.get(remainder[-2])))
        elif len(remainder) == 1:
            result.append('0' + str(conversion.get(remainder[-1])))
        else:
            result.append('00')
    return ''.join(result)


def div(y):
    remainder = []
    while y != 0:
        x = y % 16
        remainder.append(x)
        y = int(y / 16)
    if len(remainder) == 2:
        print(str(conversion.get(remainder[-1])) + str(conversion.get(remainder[-2])))
    elif len(remainder) == 1:
        print('0' + str(conversion.get(remainder[-1])))
    else:
        print('00')


print(rgb(148, 0, 211))
