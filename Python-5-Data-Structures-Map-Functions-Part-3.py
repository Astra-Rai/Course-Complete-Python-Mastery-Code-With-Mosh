# map list using map function and lambda function
# below each itemin list is a tuple of two items

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# map(functions, *interables)--> map object
# map function will apply lambda() on each item in list
# map() will iterate over 'items' list and call lamda function on each item of the iterable
# item[1], item in list index '1'x
prices = list(map(lambda item: item[1], items))
# map function returns a map object: <map object at 0x7f08900db610> ,
# map object is a interable, iterate over it using a for in loop, or convert map object into a list object

print((prices))  # output: [10, 9, 12]
