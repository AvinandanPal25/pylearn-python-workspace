# SEQUENCE TYPE DATA --> STRING, LIST, TUPLE, RANGE (later)

## COMMON OPERATIONS ~
###  Order - Length - Indexing - Slicing - Iteration - Membership nature - Concatenation - Repetition - Comparison
#=======================================================================================================================

string = "PyLearn-2"
lst = [5,11,17,2,25,2,16,8]
tup = (1,17,18,9,4)

# 1. Length - using len() we can find no of items (or characters, in case of string) in each of the sequence types
print(f"Length of string: {len(string)}, length of the list: {len(lst)}, length of the tuple: {len(tup)}")

# 2. Indexing: Each of the sequence types can be indexed in the same way, using positive and negative index.
print(string[2], lst[len(lst)-1], tup[-3]) #if out of bound - gives IndexError

# 3. Count: Using count() we can find the count of an item or substring in a sequence type data - if not present, returns 0
print(f"2 appears {string.count('2')} times in {string}")
print(f"2 appears {lst.count(2)} times in {lst}")
print(f"2 appears {tup.count(2)} times in {tup}")

# 4. Index: Using index() the index of the very first occurrence of an item or substring can be fetched
print(f"2 appears at pos.{string.index('2')} in {string}")
print(f"2 appears at pos.{lst.index(2)} in {lst}")
# print(f"2 appears at pos.{tup.index(2)} in {tup}") --> ValueError: tuple.index(x): x not in tuple
# print(f"2 appears at pos.{lst.rindex(2)} in {lst} from right") --> rindex, find, rfind are only applicable to strings

# 5. Membership Operation: in & not in ~ Using this operators we can know whether an element is part of any sequence type data or not ~~ returns Boolean value
print(25 in lst)
print(25 not in tup)
print("p" in string)
print(5 in [1,2,3, [4,5]])

# 6. Concatenation: All of them exhibits concatenation, and creates a new sequence data
"Py" + "Learn" #PyLearn
[1,2]+[3] # [1,2,3]
# (2,5)+(8) #Error - as (8) is a number, not tuple. Both operands must be of same datatype.
# [1,2,3,[4,5]] + (3,) #error again, for above reason.

# 7. Repetition: Using * operator we can create multiple copies, and sort of repeat the sequence type data.
                # * followed by no. of time it's to be repeated. placing a negative value makes the sequence empty.

print("lub-dub "*4, "teeeeeeeeee") #he is no more, RIP
print([2,3]*2)
print((8,)*7)

print([39,32,54,76]*-2)
print("empty me"*-1)

# 8. Equality and Identity: All sequence types exhibit these properties.
    ## == checks the value, and type of the two operands. is checks its values, addresses, and datatypes.

print([1,2] == [1,2])
print([1,2] == (1,2))
print([1,2] == [2,1]) #Order matters in sequence type data
print((8,) == (8)) #see the COMMA matters in tuples

# 9. Sequential Traversal: 
        ## the same order that the sequential data was defined, is maintain throughout, until explicitly changed.

for char in string:
    print(char)
print()
for item in lst: print(item)
print()
for _ in tup: print(_)


# 10. Slicing: sequence[start : stop : step] ~ each sequence object can be sliced the same way to find a substring or part of the original sequence.
fav_ipl_duo=[18,17,"Virat Kohli", "ABD", "Destruction", 'RCB', 'My_fav?',True]
print(fav_ipl_duo[:4])
print(fav_ipl_duo[5:])
print(fav_ipl_duo[:3])
print(fav_ipl_duo[2:])

print(fav_ipl_duo[-6:-2])
print(fav_ipl_duo[1:-1:2])
print(fav_ipl_duo[-2:-7:-3])
print(fav_ipl_duo[-2:-6:2])
print(fav_ipl_duo[::-1])

# exact same behavior shown by a tuple or a string.
print((2,3,4,5,1,6,9.3,7)[3:-1:3])
print("abcdefghijklmnop"[::4])

# more tricks with slicing ~
num_list=[3,2,5,1,8,4]
print(num_list)
num_list[2:5] = [8,7,6] #updating several items in a list
print(num_list)
num_list[8:] = [] # removing several items from a list
print(num_list)
num_list[:] = [] #clears the whole list
print(num_list)