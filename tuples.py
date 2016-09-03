"""
PYTHON DATA STRUCTURES

TUPLES

AUTHOR: THOMAS EGGENBERGER

 A tuple is a sequence of values separated by commas.
 A tuple has an arbitrary but finite length.
 Tuples are immutable (values cannot change).
 We cannot append or insert elements in a tuple.
 We cannot delete elements from a tuple.
 We cannot change an element of a tuple.
 Tuples are immutable, lists are mutable.
 Tuples are faster than lists.
"""


from termcolor import colored


########################################################################################################################
#EXAMPLE 1
print(colored('EXAMPLE 1:', 'red'))
print(colored("Tuples may or may not be wrapped in parenthesis ", "blue"))

my_tuple = (233, 29, 17)

print(my_tuple)

print("\n")
########################################################################################################################




########################################################################################################################
#EXAMPLE 2
print(colored('EXAMPLE 2:', 'red'))
print(colored("Tuples are 0 indexed ", "blue"))

print("index 0: {}".format(my_tuple[0]))

print("index 1: {}".format(my_tuple[1]))

print("index 2: {}".format(my_tuple[2]))

print("\n")
########################################################################################################################




########################################################################################################################
#EXAMPLE 3
print(colored('EXAMPLE 3:', 'red'))
print(colored("Find the length of a tuple ", "blue"))

print("The length of my_tuple is: {}".format(len(my_tuple)))

print("\n")
########################################################################################################################




########################################################################################################################
#EXAMPLE 4
print(colored('EXAMPLE 4:', 'red'))
print(colored("Nest a tuple within another tuple or list containing many different data types ", "blue"))

my_nested_tuple = (my_tuple, "string", 3.333, [1,2,3])

print("This tuple contains a nested tuple, a string, a float and a list: {}".format(my_nested_tuple))

print("\n")
########################################################################################################################




########################################################################################################################
#EXAMPLE 5
print(colored('EXAMPLE 5:', 'red'))
print(colored("Assign multiple values to a tuple ", "blue"))

my_brew = ("IPA", 9.6, 22)

brew_type, abv_percentage, fluid_oz = my_brew

print("My favorite brew is a dark {}.".format(brew_type))
print("It has a ABV of {} percent.".format(abv_percentage))
print("It sold in a {} bottle.".format(fluid_oz))

print("\n")
