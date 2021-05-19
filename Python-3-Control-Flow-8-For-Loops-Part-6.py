
# for in loop, range() function
# exercise 1: send message to your, if msg not delivered, try 3x'set
# A for loop is used for iterating over a sequence
# range (start, stop, step)
# start: optional, default 0
# stop:  required
# step: optional, default 1
for number in range(1,10,2): # start at 1, print attempts: 1,3,5,9

  print("Attempt", number, number *".")

# (number + 1) * "."
# string multiplied by a number results in string being repeated that number of times

# output:

#   Attempt 1 .
#   Attempt 3 ...
#   Attempt 5 .....
#   Attempt 7 .......
#   Attempt 9 .........

