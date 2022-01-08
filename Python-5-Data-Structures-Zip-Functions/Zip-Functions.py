list1 = [1, 2, 3]
list2 = [10, 20, 30]

#print(list(zip(list1, list2)))
#print((zip(list1, list2))
#<zip object at 0x10cf82a80>, zip obj not past to build in to list function to return it to a list 

#zippedResult = print(list(zip(list1, list2)))
#print(zippedResult)
#returns [(1, 10), (2, 20), (3, 30)]


"""
zip() function returns a zip object, which is an iterator of tuples where the first item
in each passed iterator is pair together, and then the second item in each passed
iterator are paired together

"""
#clearprint(list(zip("abc", list1, list2)))  

print(list(zip(list1, list2)))