# xargs
# create a function that takes a variable number of arguments
# plural number(s), indicates that there is a collection of arguments

# example 2 code: pass multiple arguments ...
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
    print(numbers)

print(multiply(2,3,4,5)) # result, line 1: (2,3,4,5), line 2: None


# example 1 code: cannot pass multiple arguments 
#   def multiply(x,y):
#     return x * y # note no (), print w/in function don't forget () else this will be a SyntaxError
#   print(multiply(2,3))
