
# global variable, example of bad practice, don't do this
# modifying the global variable from inside a function??? why do this

message = "a"


def greet(name):

    # use global keyword and reference variable 'message'
    # when Python sees this line,it will realized that in the greet() function you want to use the global msg variable ...
    # ... so it will not define a local varible in this funciton
    global message
    message = "b"  # the value of the global 'message' variable


greet("Astra")
print(message)   # output: b
