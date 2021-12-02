# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.
text = [1, 2, 3, 4, 4, 1, 2, 3, 4, 5, 5, 6, 6]


def find_it(seq):
    count = {}
    for x in seq:
        count.setdefault(x, 0)
        count[x] += 1
    print(count)
    for y in count:
        if count[y] % 2 != 0:
            return count.get(0, y)


print(find_it(text))


def find_it_oter(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i
