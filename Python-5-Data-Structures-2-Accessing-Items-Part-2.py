letters = ["a", "b", "c","d"]
letters[0] = "A"
print(letters) # output: ['A', 'b', 'c', 'd']

# use 2 indexes to slice a list
# start at 0 index, include 0, 1, 2, not three

print(letters[0:3]) # returns new list w/1st three items; ['A', 'b', 'c']

# original list not change

# letters[:3] # same result as code on line #13
# letters[0:] # end index not included, by default, length of list used
# expression online 17 will return all the items in the list
# letters[:]  # copy of original list

# list slicing article: https://www.geeksforgeeks.org/python-list-slicing/