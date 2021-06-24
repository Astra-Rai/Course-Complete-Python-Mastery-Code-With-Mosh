#   swap two variables

x = 10  # print(x), output: 10
y = 11  # print(y), output: 11

#   to solve, we need a 3rd variabl, z
#   z = x, copy value of x, using
#   assign x to y
#   assign y to z

z = x  # print(z), output:  10
x = y  # print (x), output: 11
y = z
print("x", x)
print("y", y)


