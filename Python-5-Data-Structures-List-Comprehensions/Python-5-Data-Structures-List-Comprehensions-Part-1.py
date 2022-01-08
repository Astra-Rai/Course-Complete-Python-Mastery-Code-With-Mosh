items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

#loop trough using a list comprehension and store the value of items in the 1st index in 
#list comprehension is a syntactic construct creating a list based on an existing list

prices = [item[1] for item in items]
filter = [item for item in items if item[1] >=10] #iterate through items list, check if any product is 10 or more, store in filter variable

print(prices) #output: [10, 9, 12]
print(filter) #output:  [('Product1', 10), ('Product3', 12)]
#for large list w/one million elemnts,filtering w/list comprehension is forty percent faster than the filter method
#filter returns an iterator not a list, research more about iterators