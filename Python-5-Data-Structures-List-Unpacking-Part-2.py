

# when you want to get individuals items in a list and assign them to a variable
# number of variables on the lest side of assignment operator should be equal to # of items in list

numbers = [1, 2, 3, 4, 4, 4, 4, 4]

first, second, *other = numbers # parameter prefixed with astrisk, python will get arbiturary arguments and pack them into a list

print(numbers)  # output:   [1, 2, 3, 4, 4, 4, 4, 4]    unpacking
print(first)    # ouput:    1                           seperate packing 
print(other)    # output    [3, 4, 4, 4, 4, 4]          seperate packing


#   example 1:

#       numbers = [1, 2, 3]
#       first = numbers[0]
#       second = numbers[1]
#       third = numbers[2]

#       print(numbers)
