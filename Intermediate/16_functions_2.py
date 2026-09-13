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
#------------------------------------------------------------------------------------------------------------------------------------------

# LAMBDA FUNCTION: A compact way of creating a function that has one expression whose result is the function return. It's anonymous
'''
lambda x:x**2 
is a compact way of writting 
def sqaure(x): 
    return x**2

lambda with simple conditions:-
lambda x, y: x if x > y else y
'''
print((lambda x:x**2)(4)) #the lambda function should be enclosed within parenthesis... otherwise a lambda OBJECT would be return, not the result of the function
print((lambda x, y: x if x > y else y)(18,17))


result = []
def process(numbers_list):
    for x,y in numbers_list: 
        result.append((lambda x,y: (x+y)*(x-y))(x,y))
    return result

    # # OR, assign the lambda funct to an identifier and use it
    # asquare_minus_bsquare = lambda x,y: (x+y)*(x-y)
    # for x,y in numbers_list: 
    #     result.append(asquare_minus_bsquare(x,y))
    # return result

print(process([(4,2), (8,5), (7,10)]))

#-----------------------------------------------
# MAP - FILTER - REDUCE

## Map: applies the same operation to every item of an iterable.
odd_nums = [1,3,5,7,9]
print(map(lambda x: x**3, odd_nums)) #returns a map object (an iterator)
print(list(map(lambda x: x**3, odd_nums)))

# print(list(map(lambda x,y : (x+y)*(x-y), [(4,2), (8,5), (7,10)]))) #--> TypeError: <lambda>() missing 1 required positional argument: 'y'
# If the lambda requires more than one operands - map throws an error as it expects onlt one ---> we need to use starmap
from itertools import starmap
print(list(starmap(lambda x,y : (x+y)*(x-y), [(4,2), (8,5), (7,10)]))) #starmap() effectively unpacks each tuple before passing it to the function

# Or use indexing
print(list(map(lambda num : (num[0]+num[1])*(num[0]-num[1]), [(4,2), (8,5), (7,10)]))) #--> num is each inner tuple.


## Filter: Selects only the items that satisfy a condition in an iterable
rand_nums = [153, 370, 407, 509, 1092, 1634]

def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    total_sum = sum(int(digit) ** num_digits for digit in num_str)
    return total_sum == num

print(filter(is_armstrong, rand_nums))
print(list(filter(is_armstrong, rand_nums)))


## Reduce: Applies a function cumulatively to the elements of an iterable and returns a single final value
from functools import reduce
result = reduce(lambda a, b: a+b, odd_nums) #here between a & b, one is the accumulator, the other is the current item.
print(result)

a = [5, 9, 3, 12, 7]
r = reduce(lambda x, y: x if x > y else y, a) #largest number in a
print(r)
print("-"*40)

#-------------------------------------------------------------------------------
# CLOSURES

def make_counter(start=0):
    count = start  # Enclosing variable
    
    def incr_count():
        nonlocal count        
        count += 1
        return count
        
    return incr_count #incr_count func is the closure, it retains its enclosing scope variables

count_from_0 = make_counter() #even if make_counter() is completed, this returned func retains access to the enclosing `count` var. And modifies in subsequent calls.
 
count_from_100 = make_counter(100) #a separate `count` var for a separate closure function object

# but above two are just a closure creation.

print(count_from_0()) #1
print(count_from_0()) #2 

print(count_from_100()) #101
print(count_from_100()) #102
print(count_from_100()) #103 #Multiple closures can have independent state
print()

#Examples:

def configure_api_client(base_url):
    def get(endpoint):
        return f"GET {base_url}/{endpoint}"
    
    return get

sports_api = configure_api_client("https://global.sports.com")
weather_api = configure_api_client("https://weather.com")

'''basically sports_api is -- 
def get(endpoint):
  return f"GET "https://global.sports.com"/{endpoint}"
'''

print(sports_api("sport/cricket")) #sports_api <==> get
print(weather_api("forecast"))
print()
#---------------------------------------------------------------

def make_cleaner(strip=True, lowercase=False, split_char = ""):
    def clean(value):
        if strip:
            value = value.strip()
        if lowercase:
            value = value.lower()

        if split_char:
            value = value.split(split_char)[0]
        return value

    return clean

clean_name = make_cleaner() #strip, lowercase etc are passed when creating the special `make_cleaner` func
clean_email = make_cleaner(lowercase=True)
clean_username = make_cleaner(split_char='@')

#but these arguments are passed to the closure function, that still has info about strip/lowercase set above through make_cleaner
name = "   Jannik Sinner   "
email = "  SINNY_JANNIK_atp1@tennis.com"
p_name, p_email, p_username = clean_name(name), clean_email(email), clean_username(email) 
print(f"{p_name=}, {p_email=}, {p_username=}")