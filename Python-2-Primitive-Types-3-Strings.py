# strings
# Python-2-Primitive-Types-3-Strings.py

course = "Python Programming " # can use single or double quotes to wrap around a string

# function: piece of code for repeatable tasks
# python has built in filter
# () means you are calling functions
# inputs to functions are arguments

print(course)
print(len(course)) #prints 18, note character space is counted as a character

# access to a specific character of string use [] notation
print(course[0]) #prints uppercase 'P'

# a negative index will give last elment of string
# if ZEREO represent the first character in the string then it makes sense that -1 represents the last character of the string...um...i think ???

print(course[-1]) # prints lowercase 'g'

# note if there is a character space at end of string, for example: "Python Programming ", there will be no output 

#print first three characters of string
#print(course[0][3]), if colon not added b/t course[0 RIGHT HERE 3] index error: string index out of range
# character at end index not included
# [:3], by default pyton will put zero in place of missing index number
# if start and end index not include, will return original copy of string [:]


print(course[0:3])
print(course[0:]) #ZERO index to entire string




message = """ 

Hi, Astra

How are you

""" # tripple quotes are used to format a long string