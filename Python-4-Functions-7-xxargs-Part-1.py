# xxargs
# pass multiple key value pairs to a function
# pass multiple keyword arguments to a function
# def multiply (*numbers), syntax to pass a variable number of arguments to a function


# create a function to save information about a user

def save_user(**user):
    print(user)
save_user(id=1, name="Astra", age=38) # pass in arbitary amount of key value pairs
# output: {'id': 1, 'name': 'Astra', 'age': 38}