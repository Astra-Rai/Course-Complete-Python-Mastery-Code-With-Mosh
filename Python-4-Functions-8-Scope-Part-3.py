
# scope: refers to a region of the code where a variable is defined
# global variable is accessible anywhere w/in this file
# message variable can be used inside or outside of the greet() function
# gloabl variables stay in memory for a longer period of time than local variables
# best practice: create functions with parameters and variables that are local
message = "a"

def greet(name):
    # new value assigned to message variable
    message = "b" #pylint: unused variable message, python interpreter treats message v

greet("Astra")    
print(message)   # 'a' print, Ptyhon interpreter treats message as a local variable in greet function even though it has same name as global varialbe???