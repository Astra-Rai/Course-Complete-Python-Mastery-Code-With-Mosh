
# scope: refers to a region of the code where a variable is defined
# message is a local variable w/in the greet function


def greet():
    message = "a" # scope of message variable is the greet() funciton

 print(message) # if we attempt to print(message) outside of scope, NameError: message is not defined

# we can have another function w/the same parameter and variable name outside of the greet() fucntion