

items = [
    ("Product", 10),
    ("Product", 9),
    ("Product", 12),
]


# convert output to lists

# filtered_items = (filter(lambda item: item[1] >= 10, items))
# <lambda> at 0x7f25ca7671f0>

filtered_items = list(filter(lambda item: item[1] >= 10, items))

# filter(function, iterable)
# The filter() function returns an iterator ...
# Were the items are filtered through a function to test if the item is accepted or not.

# output: filtered_items = (filter(lambda item: item[1] >= 10, items))

print(filtered_items)
