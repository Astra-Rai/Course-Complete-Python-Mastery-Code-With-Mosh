

# when you want to get individuals items in a list and assign them to a variable
# number of variables on the lest side of assignment operator should be equal to # of items in list

numbers = [1, 2, 3, 4, 4, 4, 4, 9]

# parameter prefixed with astrisk, python will get arbiturary arguments and pack them into a list
first, *other, last = numbers

print(numbers)  # output:   [1, 2, 3, 4, 4, 4, 4, 9]    unpacking
print(first)    # output:   1                           seperate packing
print(last)     # output:   9
print(other)    # output    [2, 4, 4, 4, 4, 4]          seperate packing


#   example 1:

#       numbers = [1, 2, 3]
#       first = numbers[0]
#       second = numbers[1]
#       third = numbers[2]

#       print(numbers)
