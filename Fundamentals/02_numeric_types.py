# NUMERIC TYPES of data in Python: int, float, complex, Boolean:-
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
age = 25
salary = 45000
weight = 79.245
PI = 3.14

print(type(age))
print(type(weight))

print(type(PI))

#Operations on int and float values
#-----------------------------------------------------------------------------------
x,y,z,a,b = 17,18,25,11,2

#Arithmatic Opn
print(x+y) #addition
print(y-z) #subtraction
print(a*b) #multiplication
print(a/b) #division

print(a//b) #floor division: discards the decimal value of the division result,and return the whole number alone: largest integer <= the division of two numbers
print(a%b) #modulus: remainder in a division
print(z**b) #power

print(divmod(11,2)) #pass divident and divisor in order -- returns division and modulus
print(pow(5,3)) #same as 5**3

print(abs(-23)) #absolute value - postive value
print(round(weight,1)) #round off till one decimal point
print(round(weight,2)) #till two dec points >=5 -> rounds off to next integer
print(round(weight)) #rounds off to zero dec point

print(3.2.__ceil__)
print(3.2.__floor__)
print(3.2.__floor__())

import math #Python's standard library for various mathematical operations, including logerthmic or trignometric
print(math.floor(3.2))
print(math.ceil(3.2))

print(math.sqrt(169)) #returns a float value
print(math.factorial(4))
print(math.cos(0)) #cos of 0 rad
print(math.e, math.pi)
print(math.cos(math.pi)) #cos of pi rad i.e. 180deg

print(bin(15)) #binary representation of 15
print(hex(15)) #hexadecimal representation
print(oct(15)) #octal
#print(bin(17.2)) #TypeError: 'float' object cannot be interpreted as an integer


#type casting
#===================
print(int('101'))
print(int(2.1))
print(float(age))
print(complex(age))


#Operations on Complex numbers
#-----------------------------------------------------------------------------------
m = 3+2j
n = 4-3j

print(m.real) #returns float
print(n.imag) #returns float

print(m.conjugate())
print(n.conjugate())

print(abs(n)) #sqrt(real**2+imag**2)
print(pow(m,2)) #(3+2j)(3+2j) = 9+ 2*3*2j +2j*2j = 9+12j-4 = 5+12j

#-----------------------------------------------------------------------------------

print(x>=y)
print(y<z)
print(x/b<a)

#Operations on Boolean values
print(True+True) #2
print(False-5)
print(True*5)
print(True)


#Boolean values are a subset of Integer class - has values as True & False
print("Bool is subclass of int? - ", issubclass(bool,int)) #here's the proof
print("True is an instance of int class? - ", isinstance(True,int))

print("PyLearn"[False]) #False::0 --> char at index=0
print("PyLearn"[True]) #True::1 --> char at index=1

print(int(True), float(False))

# That doesn't mean True is integer 1

print(True == 1) #value is same
print(True is 1) #datatype is different.


#EQUALITY vs IDENTITY
#====================
'''In Python, the equality operator (==) checks whether two objects have the same value. 
While the identity operator (is) checks whether two variables point to the exact same object in memory, and they have same datatype.'''

print(id(1), id(True))
print(type(1), type(True))


#TRUTHiness & FALSEiness
#=======================
print(bool(2))
print(bool(0))
print(bool(None))

'''Basically, 0 -- 0.0 -- '' -- [] -- () -- {} -- set() -- None -- False --> Has the characteristics of Falsiness or is False.
Anything apart from these are True or has a Truth value.'''
