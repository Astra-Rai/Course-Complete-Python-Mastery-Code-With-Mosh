# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# key=lambda, telling Python that we're defining a lambda or anonymous function
# syntax for lamba functions, ( key=lambda parameters:expression )
# we want to return items[1]

items = [

    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),

]
# short and clean way to define a function that we're only using once as an argument to another function
items.sort(key=lambda item: item[1])
print(items)  # output: [('Product2', 9), ('Product1', 10), ('Product3', 12)]
