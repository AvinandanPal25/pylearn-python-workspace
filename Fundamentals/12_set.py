'''Suppose you have a list of runs you scored in a cricket video game. How would you find the distinct scores?'''

scores = [189, 157, 183, 176, 201, 229, 157, 183, 189, 199, 193, 183, 201, 205, 248]
unique_scores = []
for score in scores:
    if score not in unique_scores:
        unique_scores.append(score)

print(unique_scores)

# Python has another data structure - set, for the same purpose.. to hold only unique values
un_scores = list(set(scores))
print(un_scores)


# Creating a set:
shirt_sizes = {'S', 'M', 'L', 'XL', 'XXl', 'F'}
print(type(shirt_sizes))

# Creating an EMPTY set:
# mt_set = {} #Incorrect - this is an empty dictionary
mt_set=set()
print(mt_set)

#-------------------------------------------------------------------------------------------

int_set={2,4,1,5,6,1,8,3,2,11,"set"}
print(int_set)  #does it sort the values of its own??
f_set={2.1,3.1,5.2,1.8,3.6,2.7,0.2,"set"}  #but the sorting did't happen here.
print(f_set)
#------------ Set is not ordered in the way the items are defined, neither does it sort the items.
# Set follows a hash table to do the ordering. It's not basically unordered, but arbitrarily ordered. Can't be determined.

mix_set={2, "set_value", "python", 3.9, True}
print(mix_set) 
''' If this is run a few times, it can be noticed that there's a different order of printing the elts in some runs, 
    and that is why set is said to be "Unordered". It has nothing to do with order. 
    It is needed mainly to have a bunch of unique elements.
    It also does not support positional indexing. Only membership approach. Only, "Is it present?" Not, "Where is it?"
'''
#-------------------------------------------------------------------------------------------

# Methods on set:

# (i). Adding items to a set:~
## add() - this adds new items to the set, which are unique. Exactly one argument expected.
skills = {"Python", "SQL"}
skills.add("AWS")
print(skills)

# int_set.add([7,2,4])  #list is an Unhashable type and it can not be passed as an elt for a set
# int_set.add({'dict_key':'dict_val'})  #similarly, dict is also unhashable, so can't be added to the set

int_set.add((3,8,1)) #Tupples and string are Hashable, and so these can be added
# int_set.add({4,7,9}) # A set itself can't be an item inside another set. Elements of a set are immutable, but set is not.


## update() - using update, multiple items can be added to a set from an iterable
skills.update(["JavaScript"])
skills.update(("ML", "MongoDB"))
skills.update("Java") #---> "Java" won't be added. Rather "J", "a" and "v" would be added. String is an iterable of characters.
skills.update({"EDA", "Web Scraping"}) #--> can update from a set too.

print(skills)
print()

#-------------------------------------------------------------------------------------------
# (ii). Removing items from a set:~
## remove() - pass the item to remove it. If not present -> KeyError
skills.remove("J")
print(skills)
#skills.remove('CPP') #KeyError

## discard() - similar to remove, but no error on item not found.
skills.discard('CPP')
print(skills)

## pop() - removes an arbitrary item from the set... not the last item. Cause there's no ordering in set.
print(skills.pop())
print(skills)
print(skills.pop())
print(skills)

## clear() - empties a set
skills.clear()
print(skills)

print()
#-------------------------------------------------------------------------------------------

# (iii). Other iterables' behaviors:

## len()
s = {2,3,5,7,2,5,3,4,2}
print(len(s)) #the unique values only

## iteration
for i in s:
    print(i)

## membership operation
print(25 in s)
print(18 not in s)

print()
#-------------------------------------------------------------------------------------------
# (iv). Set Operations:
set_1 = {1,3,5,7,9}
set_2 = {1,4,9,16}
set_3={2,5,10,33}
set_4={8,9}

## Union ~ the union of unique elements from two or more sets
print(set_1.union(set_2, set_3)) #--> {1,2,3,4,5,7,9,10,16,33} - in sone order
    
## Intersection ~ the common items in two or more sets.
print(set_1.intersection(set_2)) #--> {9, 16}
print(set_1.intersection(set_2, set_4)) #--> {9}

## Difference ~ items present in the first, but not in the latter.
print(set_1.difference(set_2)) #--> {3,5,7}  
print(set_2.difference(set_1)) #--> {4,16}
print(set_2.difference(set_1, set_3)) #--> {4,16}

## Symmetric Difference ~ items present in either sets, but not in both --> basically union of two way differences.
print(set_1.symmetric_difference(set_2)) #--> {3,5,7,4,16}

    
# ** Set Operations using operators: For Union --> |; for Intersection --> &; for Difference --> -; for symmetri_difference --> ^
print(set_2 | set_3 | set_4) #--> {1,2,4,5,8,9,10,16,33}
print(set_1 & set_2) #--> {1,9}
print(set_3 - set_4) #--> {2,5,10,33}
print(set_1 ^ set_2) #--> {3,5,7,4,16}

print()
#-------------------------------------------------------------------------------------------
# (iv). Set Relations: issubset - issuperset - isdisjoint
set_5 = {1,3,5,7,9,11}
set_6 = {1,9}
set_7 = {3,5}
set_8 = {1,4,9}

print(set_7.issubset(set_5)) #are all items in set-A present in set-B
print(set_5.issuperset(set_6)) #does set-A has all items present in set-B
print(set_5.issuperset(set_8))
print(set_6.isdisjoint(set_7)) #mutually exclusive or not
print(set_6.isdisjoint(set_8))

#-------------------------------------------------------------------------------------------
set_9={14,14.0,'14'}
print(len(set_9)) # This will return 2, as 14 and 14.0 are same mathematically. 
                 # But 14 and '14' are different, so they are different, no repitition here


#===================================================================================================

# FROZEN SET - A set where we can't add or remove an item

shirt_sizes = frozenset(['S', 'M', 'L', 'XL', 'XXl', 'F'])
print(shirt_sizes)
print(type(shirt_sizes))

# shirt_sizes.pop() #no such attributes
# shirt_sizes.add('XS') #no such attributes
