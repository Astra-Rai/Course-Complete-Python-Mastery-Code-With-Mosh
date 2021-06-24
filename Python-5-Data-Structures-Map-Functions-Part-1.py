# map list of times using for in loop and filter price, second item of each tuple
# below each itemin list is a tuple of two items
items = [
  ("Product1", 10),
  ("Product2", 9),
  ("Product3", 12),
]

# create an empty array to hold prices of each product

prices = []
# for in loop iterating over a list 
for item in items: 
  #append element in current iteration in prices array 
  prices.append(item[1])
print(prices) # output: [10, 9, 12]

