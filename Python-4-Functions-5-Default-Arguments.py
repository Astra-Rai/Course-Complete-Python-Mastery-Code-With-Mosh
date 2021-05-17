# default arguments
# function parameters can be optional
# all optional parameters should come after last required parameter
 
# exammple: in increment function, we don't want to explicity pass by =1 every time we increment the function
# if we call function w/o 2nd argument (ex print(increment2)), default value used (by=1)

def increment(number,by=1):
    return number + by

print(increment(2))# output 3, default parameter, by=1, used 
print(increment(2,5))# output 7, default argument, by=1, not used 