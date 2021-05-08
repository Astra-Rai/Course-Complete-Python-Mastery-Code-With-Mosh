
# Python-3-Control-Flow-5-Short-Circuit-Evaluation.py 


# in python logical operators are short circuit: if, an and and not

# pytho evaluates expression left to right, starting with first argument, if 1st value true, the second argument evaluated and so on.
# evaluation stops when one agrument is false

# elibible for loan if: high income, good credit, not a student

high_income =  False
good_credit =True
student = True

# if one of the arguments is false, code is not excusted
if high_income and good_credit and not student:
  print("Eligible")

# Short-circuit evaluation, minimal evaluation, or McCarthy evaluation (after John McCarthy) is the semantics of some Boolean operators in some programming languages in which the second argument is executed or evaluated only if the first argument does not suffice to determine the value of the expression: when the first argument of the AND function evaluates to false, the overall value must be false; and when the first argument of the OR function evaluates to true, the overall value must be true.

# with or operator we have the same concept with or and or not operators

# with or, at least one of argument should be True
# if first arument is false, python interpreter it continues, in hopes to find an argument that is True

if high_income or good_credit or not student:
  print("Eligible")
