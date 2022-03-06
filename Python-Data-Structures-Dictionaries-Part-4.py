

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


# check if key exists
# if you don't have item with key "return 0 by defalut"

# print(point["a"]) # output: KeyError a ... we need a workaround
#if "a" in point:
 #   print(point["a"])#nothing prints



# dict() check for key using get method

print(point.get("a", "key not in dicionary")) # if key not in dictionary point, by default 'None' returns
#retuns string: "key not in dictionray instead of None"
#thought, what if something is true you want 0, then false 1 = to use binary....zeros and one like twitter sentiment project
# just thinking aloud