# types of functions
  #1 function that performs a task
  #2 function that returns a value
  
def greet(name): # function performs a task
  print(f"Hi {name}") # return a formated string
  # function greet() only allow us to print something in the terminal
  # if we wanted to write the message in a file or send in an email, we'd have to create another function
  # greet () function cannot be reused in other scenarios

def get_greeting(name):
  return f"Hi {name}" # not tied to printing something on the terminal like greet() function

# because function returns a value...
# we can store function in a seperate variable
# call function and store code in a variable, message

message = get_greeting("Astra Rai")
# use built in open function to write 'message to a file'

message = get_greeting("Astra")
file = open("content.txt", "w")
file.write(message)

# greet fun() w/only print does not allow us to use f
# message variable 'message', we can: 
# (1) print to terminal (2) write to a file (3) send in an email, etc. 
