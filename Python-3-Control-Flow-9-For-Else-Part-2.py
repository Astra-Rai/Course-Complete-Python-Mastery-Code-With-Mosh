

# what if we attempt three times and still canonot send email?
# send a different message to the user and say, "we tried 3xs and it didn't work"

successful = False # variable successful set to Boolean value False simulates message unable to send after three attempts
for number in range(3): # range function creates a sequence of numbers from 0 - 3, increments by 1 by default
    print("Attempt") # print 'Attempt notification' up to three times
    if successful: # if attempt is successful, successful = True
        print("Successful") # print the string 'Successful'
        break # break out of for in loop
else: # attemptted three times, send notification to user
    print("Attempted three times and failed homie? What's goood?") # "where you at, fam?"

    
