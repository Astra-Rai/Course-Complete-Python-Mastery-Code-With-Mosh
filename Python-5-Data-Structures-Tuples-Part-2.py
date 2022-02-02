
from ctypes import pointer


point = (1, 2, 3)

if 7 in point:
    print("exists")
else:
    print("not in tuple")

# tuples, link list? no methods to add a new object or remove existing object
# tuples are useful for list of sequenced objects that you don't want to modify a
# usefu to prevent accidential errors