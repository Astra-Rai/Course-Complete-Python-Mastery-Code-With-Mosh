
items = [

    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),

]

# define a function that python will use for sorting lists
# sort items based on price
# item[1], # returns price 
# function takes an item and returns its price

# pass function when sorting list of items
# first paramenter of sort function is key, this is where we pass our sorting function
# not calling function, passing reference to funcion

def sort_item(item):
    return item[1]

# itmes.sort(sort_item)
# TypeError: sort() takes no positional arguments

items.sort(key=sort_item)
print(items) #output: [('Product2', 9), ('Product1', 10), ('Product3', 12)]

# list made up of tuples cannot be sorted usings, items.sort