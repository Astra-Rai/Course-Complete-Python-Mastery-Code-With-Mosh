# Logial Operators
# Use of: if statement, else statement logical operator 'or'
# In python we have 3 complex operators
# Operators used to model more complex conditions: and, or, not

# Example: Buidling an application processings
# Loan is processed if client has high_income and good_credit. Both represent by boolean value: 'True'
# with 'and' operator both condition must be True
# with or operator, only one condition must be true

high_income = False
good_credit = False

if high_income or good_credit:
    print("Eligible")
else:  
    print("Not Eligible")
