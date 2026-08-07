# Creating a tuple:
#===================
empty_tup = ()
tup = (8, 5, 9)
single_valued_tup = (5,) # (5) would be wrong, type becomes int. 
# t = 5, # ---> this is a tuple too.
# ** "It's the comma that defines a tuple, not the parenthesis."

het_tup = 2.5, "is half of", 5, True, (0,1), [17,18]
vowels= tuple('aeiou')
articles= tuple(['a', 'an', 'the'])
duplicate_tup = (2,1,5,4,3,5,9)


# length & Indexing a tuple:
#============================
print(len(het_tup))

print(vowels[2])
# print(vowels[5]) #Index out of range
print(vowels[-1])

# Methods on Tuples:
#====================

# Adding or removing items to a tuple: can't do it. Tuples are immutable. --> 'tuple' object does not support item assignment
# vowels[2] = 'p'

# though this can be done -
het_tup[-1].append(25) #the objects stored inside a tuple can't have a changed memory address
print(het_tup)


# count() & index()
print(duplicate_tup.count(5))
print(het_tup.count(17))

print(articles.index('a')) #first instance of the item
# print(articles.index('o'))  #raises error as not found
