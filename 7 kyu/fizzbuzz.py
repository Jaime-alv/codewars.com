# "FizzBuzz" is a well-known programming assignment, often used as a little test to see if a candidate for a programming
# job could manage to implement a set of requirements, usually on the spot. The requirements are these:
#
# Given a list of numbers from 1 to n.
# If a number is divisible by 3 should be replaced with Fizz.
# If a number is divisible by 5 should be replaced with Buzz.
# If a number is divisible by 3 and by 5 should be replaced with FizzBuzz.


def fizzbuzz(top_number):
    result = []
    for number in range(1, top_number + 1):
        if number % 3 == 0 and number % 5 == 0:
            result.append('FizzBuzz')
        elif number % 3 == 0:
            result.append('Fizz')
        elif number % 5 == 0:
            result.append('Buzz')
        else:
            result.append(number)
    return result


def one_liner(top_number):
    return ['FizzBuzz' if (number % 3 == 0 and number % 5 == 0) else 'Fizz' if number % 3 == 0 else 'Buzz' if number % 5 == 0 else number for number in range(1, top_number + 1)]


