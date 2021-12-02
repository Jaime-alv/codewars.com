# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other
# items. We want to create the text that should be displayed next to such an item.
#
# Implement the function which takes an array containing the names of people that like an item. It must return the
# display text as shown in the examples:
#
# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
# Note: For 4 or more names, the number in "and 2 others" simply increases.
test = ["Alex", "Jacob", "Mark", "Max", 'wwooo']


def likes(people):
    if len(people) == 0:
        return "no one likes this"
    elif len(people) == 1:
        return f'{people[0]} likes this'
    elif len(people) == 2:
        return f'{people[0]} and {people[1]} like this'
    elif len(people) == 3:
        return f'{people[0]}, {people[1]} and {people[2]} like this'
    elif len(people) > 3:
        other = len(people) - 2
        return f'{people[0]}, {people[1]} and {other} others like this'


print(likes(test))
