# print 1 to 10
for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)

# How about printing 1 to 50? --> A list with values from 1 to 50?
#     NO WAY. Range comes to our rescue here.

for i in range(50): # 0 till 49
    print(i)

for i in range(1,21): # 1 till 20
    print(i, end = " ") #parameter in print(), to print the nex item after a space, instead of '\n'

#range with step:
for i in range(1,50,5): # every 5th item between 1 and 50(excluded)
    print(i)


#SEQUENCE OPERATIONS on RANGE
custom_range = range(1,100, 3)
print(custom_range)
print(list(custom_range))
print(len(custom_range)) #length
print(custom_range[3]) #indexing
print(custom_range.index(28)) #index() -- if not found error -> ValueError: 27 is not in range
print(custom_range.count(5)) #always gonna be zero or one, as no duplicates.

print(custom_range[2:11:-1]) #slicing

print(5 in custom_range, 'and', 18 not in custom_range) #membership operator

print(custom_range == range(1,100,3))
print(custom_range is range(1,100,3)) #equality and idenitity


#ALL OPEATIONS BUT - concatenation & repetition
# print(custom_range+range(100,105)) #TypeError: unsupported operand type(s) for +: 'range' and 'range'
# print(custom_range[1:3]*4) #TypeError: unsupported operand type(s) for *: 'range' and 'int'

# custom_range[2] = 5   #TypeError: 'range' object does not support item assignment -- IMMUTABLE, like strings, and tuples

#Other properties
print(custom_range.start)
print(custom_range.stop)
print(custom_range.step)


# USE CASES:-
#Print all the multiples of 3 between 0-100
multiples_of_3 = []
for i in range(3,100,3):
    multiples_of_3.append(i)

print(multiples_of_3)

s = "PyLearn"
for i in range(0,len(s),2):
    print(s[i], end="") #worst ever example, I know, but tried to show an usecase.
