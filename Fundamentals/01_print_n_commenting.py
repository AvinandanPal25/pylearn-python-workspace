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

# Rules for variables: can include alphabets, numbers (not at the start), and _; should not be a keyword like for, switch, and, etc.
# Also, variables are strictly case-sensitive. age, Age, and AGE are all different variables.
var = "I am a string"
print(var)
var = 17
print("`var` is now a number", var)  

# -------------------------------------------------------------------------------------------------

# datatype of a variable

print(type(var)) #becomes int, at line #29, it was str

# Python is dynamically typed:~
# =============================
'''Variables are not bound to a fixed data type. 
   A variable can be reassigned to values of different types during program execution. 
   The type belongs to the object (value), not to the variable, i.e. it is determined by the type of the object it currently refers to.'''

# -------------------------------------------------------------------------------------------------
print(1+"2") #TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Python is Strongly typed :~
# ===========================
# Will not automatically or implicitly convert incompatible data types during an operation.
