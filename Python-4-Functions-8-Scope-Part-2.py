
# scope: refers to a region of the code where a variable is defined
# message is a local variable w/in the greet function
# local variables have a short life time




def greet(name):
    message = "a"  # scope of message variable is the greet() funciton

 print(message) # if we attempt to print(message) outside of scope, NameError: message is not defined

# when greet() function is called and argument is passed, Python interpreter will allocate memory and...
# have the 'name' and 'message' variables reference those memory locations 
# when the greet function is fully executed ...eventually they will get garbage collected
# translation: python interpreter will release the memory allocated to variables, in this case (name and message)




# scope, local variables,garbage collection, memory