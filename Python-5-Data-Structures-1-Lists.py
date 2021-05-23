  
# in python every object of a list can be a different type 
letters = ["a", "b", "c"] # list of one character strings
matrix = [[0,1], [2,3]]# a 2-D list, a list w/in a list 
zeros = [0] * 5
combined = zeros + letters # use + to concatenate mulitple lists
# print(combined) # output: [0, 0, 0, 0, 0, 'a', 'b', 'c']
# list of numbers up to 20, use list function
# list function takes an interable, pass iterable and convert it to a list 
# range()function returns a range object which is iterable# 
# range(20), creates a list of numbers from 0 to 19
numbers = range(20)

for number in numbers:
  print(number)# 1 - 19, each integer printed, vertically

numbers1 = list(range(20))
print(numbers1) # output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

chars = list("Hello World") # each character in original stringis an item in the list 
# get number of items in list using len() function
print(len(chars)) # output: 11