# Trolls are attacking your comment section!
#
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the
# threat.
#
# Your task is to write a function that takes a string and return a new string with all vowels removed.
#
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
#
# Note: for this kata y isn't considered a vowel.

string_v = "This website is for loooooosers LOL!"
spam = 'Hello'
string_test = 'OOOsesom gmoesqweoeaius oreegmEEE'


def disemvowel(string_):
    vowel = ['a', 'e', 'i', 'o', 'u']
    string_list = list(string_)
    end_string = []
    for x in string_list:
        if x.lower() in vowel:
            continue
        else:
            end_string.append(x)

    string_ = ''.join(end_string)
    return string_


def disemvowel_byother(s):
    for i in "aeiouAEIOU":
        s = s.replace(i, '')
    return s


print(disemvowel(string_v))
print(disemvowel_byother(string_v))

"""
def disemvowel(string_):
    vowel = ['a', 'e', 'i', 'o', 'u']
    string_list = list(string_)
    while True:
        for x in string_list:
            if x.lower() in vowel:
                string_list.remove(x)
        string_ = ''.join(string_list)
        return string_


def disemvowel2(string_):
    vowel = ['a', 'e', 'i', 'o', 'u']
    string_list = list(string_)
    for x in string_list:
        if x.lower() in vowel:
            string_list.remove(x)
    string_ = ''.join(string_list)
    return string_


vowel = ['a', 'e', 'i', 'o', 'u']
vow_position = []

hello = ['h', 'e', 'l', 'l', 'o']


def hello_def(hello):
    for y in hello:
        if y.lower() in vowel:
            hello.remove(y)

    hello_string = ''.join(hello)
    return hello_string


def index_position(string_):
    vowel = ['a', 'e', 'i', 'o', 'u']
    string_list = list(string_)
    for y in range(len(string_)):
        if string_[y] in vowel:
            del string_list[y]
    print(string_list)

"""
