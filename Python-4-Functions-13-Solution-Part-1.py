
def fizz_buzz(input):
    if input % 3 == 0: # if input is divisible by 3 w/o a remainder, return the string "Fizz"
        return "Fizz"
    if input % 5 == 0: # if input is divisible by 5 w/o a remainder, return the string "Buzz"
        return "Buzz"
    if (input % 3 == 0) and (input % 5 == 0): # if input evenly divisible by 3 and 5, return the string "Fizz Buzz"
        return "Fizz Buzz"
    else:
        return "{} : Not evenly divisible by 3, 5, nor simultaneously evenly dividle by 3 and 5".format(input)    
print(fizz_buzz(7))


# I expected this to return the string'Fizz Buzz' because 15 is evenly divisible by 3 and 5
# But, the code is not ran once the first statement evalutes as true

# first version, if input % 3 == 0: return "Fizz", else return "Buzz"
# doesn't take in account if input is evenly divisible by 3 and 5
# if the value returned is a string, elif, else not necessary

