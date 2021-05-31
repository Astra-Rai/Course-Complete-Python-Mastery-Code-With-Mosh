

# use keyword argument to set value for reverse parameter
# reverse is used to set the sort order
# reverse value is boolean: True or False
# number are sorted in descending order
# sort method has two parameters (key, and reverse)
# reverse to true will order element in descending order

numbers = [1, 2, 3, 4, 5]

numbers.sort(reverse = True) 
print(numbers) # output: [5, 4, 3, 2, 1]
