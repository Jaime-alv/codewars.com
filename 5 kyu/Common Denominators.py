# Common denominators
#
# You will have a list of rationals in the form
#
# { {numer_1, denom_1} , ... {numer_n, denom_n} }
# or
# [ [numer_1, denom_1] , ... [numer_n, denom_n] ]
# or
# [ (numer_1, denom_1) , ... (numer_n, denom_n) ]
# where all numbers are positive ints. You have to produce a result in the form:
#
# (N_1, D) ... (N_n, D)
# or
# [ [N_1, D] ... [N_n, D] ]
# or
# [ (N_1', D) , ... (N_n, D) ]
# or
# {{N_1, D} ... {N_n, D}}
# or
# "(N_1, D) ... (N_n, D)"
# depending on the language (See Example tests) in which D is as small as possible and
#
# N_1/D == numer_1/denom_1 ... N_n/D == numer_n,/denom_n.
# Example:
# convertFracs [(1, 2), (1, 3), (1, 4)] `shouldBe` [(6, 12), (4, 12), (3, 12)]
# Note:
# Due to the fact that the first translations were written long ago - more than 6 years - these first translations have
# only irreducible fractions.
#
# Newer translations have some reducible fractions. To be on the safe side it is better to do a bit more work by
# simplifying fractions even if they don't have to be.
test_1 = [[77033412951888080, 14949283383840498], [117787497858828, 14949283383840498], [2526695441399712, 14949283383840498]]
should_equal = [[77033412951888085, 14949283383840498], [117787497858828, 14949283383840498], [2526695441399712, 14949283383840498]]
given = [[1, 2], [1, 3], [1, 4]]


def convert_fracts(numbers):
    import math
    lcm = 1
    for i in [x[1] for x in numbers]:
        lcm = lcm * i // math.gcd(lcm, i)
    return [[int((lcm / y[1]) * y[0]), lcm] for y in numbers]


print(convert_fracts(given))
