#  The 'in' operator is used to check if a value exists in a sequence or not


letters = ["a", "b", "c"]
if "d" in letters:
    print(letters.index("d"))
else: 
    print("letter not in list")


#   print(letters.index("a"))  # output:     0
#   print(letters.index("z"))  # output:     ValueError: 'z' is not in list
