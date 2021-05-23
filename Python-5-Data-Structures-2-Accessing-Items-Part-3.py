
numbers = list(range(20))
print(numbers)

# output of line #2 code:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# ouput every other number starting at zero and ending at 19

print(numbers[::2]) # output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

#Slicing with step Python
#slice() can take three parameters:
#start (optional) - Starting integer where the slicing of the object starts. Default to None if not provided.
#stop - Integer until which the slicing takes place. ...
#step (optional) - Integer value which determines the increment between each index for slicing.


print(numbers[::-1]) # output: [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# list slicing article: https://www.geeksforgeeks.org/python-list-slicing/