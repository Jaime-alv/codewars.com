# Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's
# divisors(except for 1 and the number itself), from smallest to largest.
# If the number is prime return the string '(integer) is prime'.
# 
# Example:
# divisors(12); #should return [2,3,4,6]
# divisors(25); #should return [5]
# divisors(13); #should return "13 is prime"

def divisors(integer):
    div = []
    for x in range(1, integer):
        if integer % x == 0:
            if (x != integer) and (x != 1):
                div.append(x)
    if len(div) == 0:
        return str(integer) + ' is prime'
    return div

def divisor(integer):
    div = [x for x in range(2, integer) if integer % x == 0]
    if len(div) == 0:
        return str(integer) + ' is prime'
    return div

print(divisors(29))
