# Pass by Reference vs Pass By Object Reference

def change_me(input_obj):
    input_obj.append(12) #when a mutable object is mutated inside the function using local parameter, the original obejct is mutated too.
    print("Added 12 to the passed object")
    print(f"The received objects is changed to - {input_obj}")

doms = [2,11]
change_me(doms)
print(f"Original list - {doms}") #[2,11,12]
print()

def change_me(input_obj):
    input_obj = [2,11,12] #Re-assignment of the passed object through local parameter won't update the original object.
    print("Assigned a new object")
    print(f"The received objects is changed to - {input_obj}")

doms = [2,11]
change_me(doms)
print(f"Original list - {doms}\n\n") #[2,11] - remains intact.


#---------------------------------------------------------------------------
# Shallow Copy & Deep Copy:=
#-----------------------------
list_1 = [25,36,49,64,81,100,121]
list_2 = list_1 #informal copy - not a new object, just a new identifier to identify the same object

list_1.append(144)
print(f"{list_1=}")
print(f"{list_2=}")  #is updated as well.
print("Both lists are updated, as both list_1 and list_2 are pointing to the same object\n")

#shallow copy is created using copy()
list_1 = [25,36,49,64,81,100,121]
list_3 = list_1.copy() # a new object is created

list_1.append(144)
print(f"{list_1=}")
print(f"{list_3=}")  #not updated
print("copy() creates a new object. So mutation is not affected in the copied object\n")

#Limitation of Shallow copy -> Shallow-level copy
list_4 = [[25,36,49],[64,81,100]]
list_5 = list_4.copy()

list_4.insert(0,[1,4,9,16])
print(f"{list_4=}")
print(f"{list_5=}\n")  #not updated

#----------------
list_4 = [[25,36,49],[64,81,100]]
list_5 = list_4.copy()

list_4[1].append(121)
print(f"{list_4=}")  #121 appended in the 2nd inner list
print(f"{list_5=}") # 2nd inner list is updated as well 
print("Copy creates a new object on the shallow level. The inner lists are still the same objects. So, mutation of inner lists are reflected in the copied object\n")

#----------------------------------------------
# Deep Copy

import copy

list_4 = [[25,36,49],[64,81,100]]
list_5 = copy.deepcopy(list_4)

list_4[1].append(121)
print(f"{list_4=}")  #121 appended in the 2nd inner list
print(f"{list_5=}") # 2nd inner list is not updated, as it also was a new object in the deeply copied object.
print("Deep Copy creates a new objects for outer as well nested objects. It thus ensures safe sharing when a data structure contains mutable objects\n")


#---------------------------------------------------------------------------------------------------
# FUNCTIONS are FIRST-CLASS Objects - can be assigned to a variable, passed as an argument, returned from another func, or stored in data structures.

## Assgining function object to a variable
def square(x): return x**2

power_of_two = square

print(square)
print(power_of_two)

print(square(3))
print(power_of_two(3))
print()

## Passing function as arg to another func
def cube(x): print(x**3)

def math_op(func, val):
    return func(val)

print(math_op(square, 5))
print(math_op(cube, 8))
print()

## Returning a func from another
def get_multiplier(factor):

    def multiply(value):
        return value * factor

    return multiply

double = get_multiplier(2) #double is a function obj
triple = get_multiplier(3)

print(double(10))
print(triple(1725))
print()

## Storing into a data structure
import math
def square_root(x): return math.sqrt(x)
def factorial(x): return math.factorial(x)

math_ops = [square, square_root, factorial]
nums = (2,4,10,16)

for op in math_ops:
    for n in nums:
        print(op(n))
    print("-"*30)
print("="*40)


opn_dict = {"Square": square, "Cube": cube, "Factorial": factorial}

for op_name, op in opn_dict.items():
    print(f"{op_name} of 10 is {op(7)}")

for n in nums:
    print(opn_dict.get('Square')(n))

print()

# A higher order function is one that accepts one or more functions as arguments and/or returns a function.. e.g. math_op, get_multiplier
#-----------------------------------------------
# LAMBDA FUNCTION:


# MAP - FILTER - REDUCE