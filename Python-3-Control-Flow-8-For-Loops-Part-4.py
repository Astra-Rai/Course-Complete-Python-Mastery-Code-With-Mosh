# for in loop, range() function
# exercise 1: send message to your, if msg not delivered, try 3x'set
# A for loop is used for iterating over a sequence

for number in range(3): # start at 0 and stop before three
#number is <class 'int'>, number increments by one with each interation

  print("Attempt", number, (number + 1) * ".")#changed first attempt from 0 to 1

# (number + 1) * "."
# string multiplied by a number results in string being repeated that number of times

# range() function returns a sequence of numbers..
# starting from 0 by default
# and increments by 1 (by default), and stops before a specified number.
