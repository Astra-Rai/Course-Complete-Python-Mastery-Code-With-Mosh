# variable 'command' set to an empty string: command =""
# while loop will execute as long as command doesnt equal string text quit"": while command != "quit"
# use built in input function to get input from user: input
# add label to input function: input(">")
# store user input in 'command' variable: command = input(">")
# ECHO back what user enter, and 'command'

command = ""
while command.lower() != "quit": # lower() will convert user input to lowercase letter, no matter how user types in word
  command = input(">")
  print("ECHO", command)