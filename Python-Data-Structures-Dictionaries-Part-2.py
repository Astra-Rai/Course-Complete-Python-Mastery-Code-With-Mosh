

### dictionary is a collection of key/value pairs
### dictionaries only use immutable types for keys, often strings and numbers used

####  point = {"x":1, "y":2} #output = 1

####  print(point["x"])

point = dict(x=1,y=2) # dictionary function, cleaner 
# index is a name of a key, dictionaries are collections of key value pair, keys cannot be acceessed with numeric index

point ["x"] = 10 #change value of x to new value
print(point) # output: {'x': 10, 'y': 2}
point["z"] = 20
print(point) # output: {'x': 10, 'y': 2, 'z': 20}
# new keys can be added, key values can be changed
