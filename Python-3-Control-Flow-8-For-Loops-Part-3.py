
# for in loop, range() function
# exercise 1: send message to your, if msg not delivered, try 3x'set
# A for loop is used for iterating over a sequence

for number in range(3): # start at 0 and stop before three
#number is <class 'int'>, number increments by one with each interation

  print("Attempt", number + 1)#changed first attempt from 0 to 1

#output: vertically: Attempt 1 Attempt 2  Attempt 3

# range() function returns a sequence of numbers..
# starting from 0 by default
# and increments by 1 (by default), and stops before a specified number.

# range(3) stop before three, 0,1,2