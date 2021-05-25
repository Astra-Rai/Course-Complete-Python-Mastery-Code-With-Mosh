
# after the 1st attempt, we can successfully send the message

# code example 1: 
#       for number in range(3): 
#           print("Attempt") 
#           
#       # output: Attempt Attempt Attempt (vertically) 


# code example 2:

# if first attempt is successfully, we want to jump out of loop
# we can jump out of loop using a break statement

successful = True # variable successful set to boolean value True to simulate msg being successful at  first attempt
for number in range(3):
    print("Attempt") # string 'Attempt' printed at least one time # this line belongs to for loop
    if successful: # this line belongs to for loop
        print("Successful") # line belongs to if statement
        break # line belongs to if statement

# code output: 
    #   Attempt
    #   Successufl
    
 # lines 18 and 19 belong to for loop
 # in every iteration of for loop, lines 18 and 19 are executed

