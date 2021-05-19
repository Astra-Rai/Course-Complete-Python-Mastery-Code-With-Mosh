# infinite loops
# infinite loop is a loop that runs forever in response to a condition whose state never changes

# break: jump out open 

# code not need: command=""
# we initialized command to an empty string b/c we had the while staement...
# while command != 'quit', we had to define the command variable ..
# without that line of code, when python tries to execute code, it doesn't know what 'command is'
# see lesson 12 on while loops for more info


while True: # true is always, condition can run forever 
  command = input(">")
  print("ECHO", command)
  # after we get input from the user
  # convert input to lowercase characters
  # check if command.lower() equals to "quit"
  # The == operator compares the value or equality of two objects

  if command.lower() == "quit":
    break
