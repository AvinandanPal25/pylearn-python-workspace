#Printing in Python - using `print` function:

print("Whatever you want")
print('Hello! How are you?')
print(1)
print("I am", 2) #I am 2
# -------------------------------------------------------------------------------------------------

# Commenting in Python - can be done in two ways: 
#   1. Single Line Commenting (using '#' symbol or by doing ctrl+/ on the particular line)
#   2. Multi Line Commenting  (using '#' multiple times, i.e. in each line of the comment
#                                      or else using ''' around anything_to_comment_out ''' )

print("The below is single line commensting in Python - the line would be ignored by Python.")
# whatever is written here will not be executed as it is commented out

print("Now this is the way to write multi-line comment in Python")
# One way is this
# where mutliple '#' symbols
# are used, or else

'''Or else You can do 
use this format for 
more convenience.'''
# -------------------------------------------------------------------------------------------------

# Variables in Python
var = "I am a string"
print(var)
var = 17
print("`var` is now a number", var)  #Python is dynamically typed
# -------------------------------------------------------------------------------------------------

# datatype
print(type(var)) #becomes int, at line #29, it was str
