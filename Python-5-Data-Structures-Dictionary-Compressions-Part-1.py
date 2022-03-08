values = []
for x in range(5):
# range function retuns a sequence/nums
# range() default 0, increments by one, stops before specified number
    values.append(x *2)
    # append method adds a single item to the existing list
    # append method doesn't return new list, modifies original list
print(values) #output: [0, 2, 4, 6, 8]  

    # 1 0 0 * 2 =   0
    # 1 1 * 2 =     2
    # 2 2 * 2 =     4
    # 3 3 * 2 =     6
    # 4 4 * 2 =     8


