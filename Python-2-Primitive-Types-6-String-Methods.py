
#string methods

#example 4 
# use in operator to check to see if we have pro in course   

course = "  python programming"
print("pro" in course)
print("swift" not in course)

# in operator returns a boolen value
# find returns the starting index of characters searched

#not operator, use to check if a string does not contain a sequence of characters

#example 3

#get index of sequence of characters, use find()
#find() argument pass a character or series of characters
# wrap find() argument in "find_argument"

# course = "  python programming"
# print(course.find("pro")) # the index of 'pro' is 9 
# if find() result is -1, this means he string was not found
# replace() can replace a character or a sequence of characters

print(course.replace("p","j")) # output: jython jrogramming

#example 2

# used to trim white space at beginning or end of SyntaxWarning
# useful for when we are receiving input from user 

#note white spaces at beginning of string
#course = "  python programming"
#print(course) #whitespace noticeable, link a tab in paragraph
# lstrip(), rstrip()
   
#print(course.strip()) # use strip() method

#example 1

#course = "python programming"
#print(course.upper()) # PYTHON PROGRAMMING
#print(course.lower()) # python programming
#print(course.title()) # Pyton Programming

