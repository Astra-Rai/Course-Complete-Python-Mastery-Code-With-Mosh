# functions: arguements
# when function is called, but argument # != to # of function parameters


# parameter: input you define for your function
# function greet paramenters: #parameters:  (first_name, last_name)
# function arguments: actual value for a given parameter
# f: formatted string

def greet(first_name, last_name):
  print(f"Hi {first_name} {last_name}")
  print("Welcome aboard")

# arguments for the greet function: "Astra", "Rai"
greet("Astra")

# if function is missing argumenet....
# TypeError: greet() missing 1 required positional arguement: 'last_name'
