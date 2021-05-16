# types of functions
  #1 function that performs a task
  #2 function that returns a value
  
def greet(name): # function performs a task
  print(f"Hi {name}") # return a formated string
greet("Astra")

def get_greeting(name):
  return f"Hi {name}"

# because function returns a value...
# we can store function in a seperate variable
# call function and store code in a variable, message

message = get_greeting("Astra Rai")
print(message)