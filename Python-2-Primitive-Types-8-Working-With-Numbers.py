#working with numbers
# round() method, abs() method

import math

print(round(2.54)) # 3
print(abs(-2.9)) # 2.9

# rounding down: 0, 1, 2, 3, 4, 5...i thought you round up at 5, python round does not, look at this again

# rouding up: 6, 7, 8 , 9

# absolute value: the magnitude of a real number without regard to its sign.

# math module,if you want to write program that writes complex mathematical computations use math ModuleNotFoundError

# math is an object, use dot notation to see all methods available in math object

# The math.ceil() method rounds a number UP to the nearest integer, if necessary, and returns the result. 

print(math.ceil(2.2)) # 3
print(math.ceil(1.4)) # 2
print(math.ceil(5.3)) # 6
print(math.ceil(-5.3)) # -5, remember -5 is greater than -6
print(math.ceil(22.6)) # 23
print(math.ceil(10.0)) #10

# note: if import math not added to code, this is the error: NameError: name 'math' is not defined

# More on math module and function resource: https://docs.python.org/3/library/math.html

