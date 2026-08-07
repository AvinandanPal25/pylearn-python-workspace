# Creating a list:
#==================
empty_list = []
fav_players = ['Kohli', 'de Villiers', 'Ashwin', 'Steyn', 'Jannik']
vowels= list('aeiou')  # ['a', 'e', 'i', 'o', 'u']
het_list = ['VK', 18, 'Indian', 52.57, [254, 183, 122], {"age": 37, "plays_test": False}]
duplicate_list = [2,1,2,4,3,2,9,2]


# length & Indexing a list:
#============================
print(len(het_list))
print(len(duplicate_list))

print(fav_players[2])
# print(fav_players[9]) #Index out of range
print(fav_players[-4])


# Methods on Lists:
#====================

# Adding items to a list: append, extend, insert
#-------------------------------------------------------

fav_players.append("Federer") #appends at the end
print(fav_players)

fav_players.extend(["Salah", "Szobozlai"])
print(fav_players)

fav_players.insert(3, "Bhuvi") #inserts at an index
fav_players.insert(20, "Robertson") #if index ot of bound --> inserts at the end
fav_players.insert(-20, None) # if negative index out of bound --> inserts at the start
print(fav_players)


# Removing/ deleting items from a list: pop, remove, clear, del
#---------------------------------------------
fav_players.pop()
print(fav_players)
popped_player = fav_players.pop(-3)
print(popped_player, fav_players)

fav_players.remove("Szobozlai")
# fav_players.remove("Szobozlai") #if not found. raises error.

del fav_players[0] #deletes the 4th item from the list
print(fav_players)

fav_players.clear() #truncates the list
print(fav_players)

del fav_players
# print(fav_players) #error as the variable to deleted from memory.


# count() & index()
#----------------------------------------
print(duplicate_list.count(2))
print(duplicate_list.count(6))

print(duplicate_list.index(2)) #first instance of the item
# print(duplicate_list.index(6))  #raises error as not found


# Rearranging methods - sort, sorted, reverse, reversed
#----------------------------------------------------------

duplicate_list.sort() #changes in the original list --- also printing it directly returns None.
# duplicate_list.sort(reverse=True)
print(duplicate_list)

# sorted(duplicate_list) #the original list is kept intact
# print(duplicate_list)

duplicate_list.reverse() #original list is changed.
print(duplicate_list)

reversed(duplicate_list) #no change to the original list
print(duplicate_list)


# Copying a list
#-------------------
todo = ['code', 'eat', 'sleep', 'repeat']
another_todo = todo #the same list referenced by two different variables
a_third_todo = todo.copy() # id() of each is different.

another_todo[-1] = "do not repeat"
print(another_todo)
print(todo) #original one changed
print(a_third_todo)

a_third_todo[-1] = "do not wake up"
print(a_third_todo)
print(todo) #original one is unchanged
print(another_todo)