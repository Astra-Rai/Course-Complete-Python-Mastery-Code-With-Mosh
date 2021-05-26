def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
     return total # if return is indented, output: 1, not 6
#line 5 if we pressed F10, we just out of function, loop didn't execute to completion
print("Start")
print(multiply(1, 2, 3))  # output: 6

# open debugging panel, click wheel widget icon when first opening debugging panel
# clicking on wheel widet will generate a new file: launch.json, file has debugging configurations
# the lauch.json file is now in the Python Debugging folder along with this file 
# in Debug-> select: Python: Current File (Integrated Terminal)

# To begin debugging...
# Add breakpoint to a statement, insert breakpoint by pressing F9 (FN + 9)
# Press F5 to run application up to breakpoint, line 8, red dot
# Press F10 to execute one statement at a time, line 9, yellow flag
# F11: Step into a function that you call
