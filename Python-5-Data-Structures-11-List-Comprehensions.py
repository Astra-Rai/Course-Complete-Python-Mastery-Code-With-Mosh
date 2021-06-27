# map and filtering list using list compressions
# list comprehestion are cleaner and more performant
# syntax: experession for items in items

# prices = list(map(lambda item: item[1], items))

items = [
  ("Product1", 10),
  ("Product2", 9),
  ("Product3", 12),
]

# prices = list(map(lambda item: item[1], items))

# using list comprehension to map a list into a different kind of lists
prices = [item[1] for item in items] # filter list, print price of each product

#[], defining a new list
# iterate over list of item, get item and return, filter if item is greater than or equal to 10

filtered = [item for item in items if item[1] >=10]
print(prices) # output = [10,9,12]