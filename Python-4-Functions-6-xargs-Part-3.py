# xargs
# functions, parameters, (*numbers), for in loop, augment assignment operator

def multiply(*numbers):
  total = 1
  for number in numbers:
      # use augment assignment operator total = total * number
      total *= number
  return total # return statments shouldn't be within code block of for loop, don't forget to use indentation properly

print(multiply(2,3,4,5)) # 2*3=6, 6*4 = 24, 24*5 = 120 