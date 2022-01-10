#LIFO: last in first ouit. think of a stack of books
#the last book placed on the stack is the first picked-up from the top
browsing_session = [] # empty list, imagine an empty browsing session
browsing_session.append(1) #append the integer 1  to empty list browsing_session
browsing_session.append(2) #append the integer 2  to browsing_session list
browsing_session.append(3) ##append the integer 2  to browsing_session list
print(browsing_session) #output  [1,2,3]
#print(browsing_session[-1]) # # output last session url , output is 3
#bookmark_last_session = browsing_session[-1] , stored in a variable to "look up" later
#print(bookmark_last_session)
last_session = browsing_session.pop()
print(last_session)
#when users presses back button, redirect them to previous website
print("redirect", browsing_session[-1])
#check if stack is empty, check, if empty disable back button
#falsy falues 0, "", not ...note i don't fully understand

#if not operator applied to empty list, the boolean true is returned

if not browsing_session:
    print("disable back button")

    



