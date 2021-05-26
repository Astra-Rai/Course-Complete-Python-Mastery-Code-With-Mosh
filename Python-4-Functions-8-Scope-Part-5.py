
# global variable, example of bad practice, don't do this
# modifying the global variable from inside a function??? why do this
# WHY THIS IS A BAD IDEA: you might have mutliply function that rely on the value ...
# ...of the global variable, changing value of global var in one function may hava a side effect in other funcitons..
# those functions might not bahave properly, this can create a bug in our program
# if you do modify a variable globally, do not modify in a function, as done in the example below


message = "a"


def greet(name):

    # use global keyword and reference variable 'message'
    # when Python sees this line,it will realized that in the greet() function you want to use the global msg variable ...
    # ... so it will not define a local varible in this funciton
    global message
    message = "b"  # the value of the global 'message' variable


greet("Astra")
print(message)   # output: b
