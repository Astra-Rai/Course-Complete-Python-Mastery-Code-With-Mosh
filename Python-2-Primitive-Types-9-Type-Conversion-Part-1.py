# input function is built in, is used to get input from user
# input argument (""), string that is displayed in terminal
# don't run program using code runner extension, 
#cre runs program in output window which is read only so you wont be able to enter a vaule, use terminal
# input from user is string value, looks like this at runtime: "1" + 1
# objects cannot be concatenated if they are not of the same type
# string "1" can be converted into a number

# example 2
# convert 'x' to an integer
#print value of y usinga formatted string
# formatted string should print both the value of x and y

x = input("enter value for x: ")
# convert x to an integer

y = int(x) + 1

# print x and y using a formatted SyntaxWarning

print(f"value of x is: {x}, value of x added to y is: {y}")

# value entered for x by user, int 8
# output: value of x is: 8, value of x added to y is: 9

#*************************************************************#

# example 1: 
# error because you cannot add a string and integer

#print(type(x)) # entered number 9, result: <class 'str'>
# x = input("x ")
# y = x + 1 # error: TypeError: can only concatenate str (not "int") to str



# built in functions for type conversion: int(), float(), bool(),str()

