# Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most
# secret question is still correct.
# However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.
# Your task is to write a function maskify, which changes all but the last four characters into '#'.
#
# Examples
# maskify("4556364607935616") == "############5616"
# maskify(     "64607935616") ==      "#######5616"
# maskify(               "1") ==                "1"
# maskify(                "") ==                 ""
#
# # "What was the name of your first pet?"
# maskify("Skippy")                                   == "##ippy"
# maskify("Nananananananananananananananana Batman!") == "####################################man!"


test = "Skippy"


def maskify(cc):
    return "#" * (len(cc) - 4) + cc[-4:]


def maskify_long(cc):
    last = []
    last_4 = ''
    if len(cc) > 4:
        n = 5
        while n > 1:
            n -= 1
            y = cc[-n]
            last.append(y)
            last_4 = ''.join(last)
        return '#' * (len(cc) - 4) + last_4
    else:
        n = (len(cc) + 1)
        while n > 1:
            n -= 1
            x = cc[-n]
            last.append(x)
            last_4 = ''.join(last)
        return last_4

print(test[-2:])
print(maskify(test))
