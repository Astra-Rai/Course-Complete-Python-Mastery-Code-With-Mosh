
from array import array #import array module
# use arrays w/a large sequenceof numbers and when you encounter performance problems

# arrays, data type filter
# take less memory and perform faster than list, greater than 10,000 
# first parameter of array, typecode
# array (typecode[, initializer]) ->
# return a new array whose items are restricted by typecode
# typecode, string that determines type of items in your array
# string of one character that determines the type of items in your list
numbers = array("i", [1,2,3])
numbers.append(5) # add value to end of array
numbers.pop() # remove value from last index of array
numbers.insert(1,9) # insert number 9 at 1st index of array, each value will shift one index
numbers.remove(33) # remove item from index in array, if item not in array: ValueError: array remove(x) x not in array
print(numbers)

# every obj in array must be of same type, if not TypeError


# This module defines an object type which can compactly represent an array of basic values:
# typecode link
# https://docs.python.org/3/library/array.html


