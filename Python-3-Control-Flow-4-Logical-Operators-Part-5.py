# Logial Operators
# Use of: if statement, else statement logical operator 'or'
# In python we have 3 complex operators
# Operators used to model more complex conditions: and, or, not

# Example: Buidling an application processings
# Loan is processed if client has high_income and good_credit. Both represent by boolean value: 'True'
# with 'and' operator both condition must be True
# with or operator, only one condition must be true
# with not operator, inverses value of boolean

# make statement more complex
# person can have high_income or good_credit, but not be a student
high_income = False
good_credit = True
student = False


if (high_income or good_credit) and not student:
#if high_income or good_credit:
    print("Eligible")
else:  
    print("Not Eligible")

# output is: "Eligible"
# REMEMBER: not student, student is initially false.. 
# now the statement not student EVALUATES to true, condition TRUE