# tuples:
# parameter of function() plural
# parameter prefixed by asterisk: *numbers
# [] used to create lists
# () used to create tuples
# tuple is similar to a list in that it is a collection of objects
# tuple collection cannot be modified
# tuples are interable, we can use them in loops
# (*numbers), multiply(2,3,4,5) crates the following touple...
# (2,3,4,5)




def multiply(*numbers):
    for number in numbers:
        print(number)

print(multiply(2,3,4,5)) # result: line 1: 2 3 4 5 (listed vertically) 


