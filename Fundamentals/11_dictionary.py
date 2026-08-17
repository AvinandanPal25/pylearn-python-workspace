# Creating a dictionary using dictionary literal:
pkt_dictionary={'Brisk':'at a very high, quick, and energetic speed', 
                'Brimming':'to be loaded or filled with something', 
                'Quintessential':'being the most typical example or most important part of something'}
print(pkt_dictionary)
print(type(pkt_dictionary))

batter_detail_dict = {"name": "Bethell", "representing_country": "England", "batting_style": "Left Handed", "age": 22, 
                        "ipl_team": "RCB", "batting_pos": "top_order", "bowling_style": "LAO"}

# Creating a dictionary using dict():
tennis_p1 = dict(player="Jannik Sinner", atp_ranking=1, nation="Italy", my_fav=True)

# Creating a dictionary using list of tuples:
data_tup = [("player", "Novak Djocovic"), ("atp_ranking", 4), ("nation", "Serbia"), ("my_fav", False)]
tennis_p2 = dict(data_tup)
# print(tennis_p1[0])  #Invalid


# Creating an EMPTY dictionary:
empty_dict={}
print(type(empty_dict))

mt_dict = dict()
print(mt_dict)

print()
#------------------------------------------------------------------------------------

# keys of a dictionary:
print(batter_detail_dict.keys()) #a view object (dict_keys obj)
# values of a dictionary:
print(batter_detail_dict.values()) #a dictionary view obj (dict_values obj)
# items in a dictionary:
print(batter_detail_dict.items()) # dict_items obj containing list of tuples

print()
#------------------------------------------------------------------------------------

# accessing dictionary value:
print('"Brisk" means: ', pkt_dictionary['Brisk'])
# print('"brisk" means ', pkt_dictionary['brisk']) #case-sensitive... key not found --> KeyError.

# accessing value using get() method:
print(f"{tennis_p1.get('player')} is ranked {tennis_p1.get('atp_ranking')}, in ATP rankings.")

print()
#------------------------------------------------------------------------------------

# Adding an item to a Dictionary:
pkt_dictionary['Famished'] = "extremely hungry or starving"
print(pkt_dictionary)

# Updating a dictionary: If the assignment is done on a key that is already present, the key's value gets updated. It doesn't create a duplicate key.
batter_detail_dict["name"] = "Jacob Bethell"
print(batter_detail_dict['name'])


# Deleting a Key value pair:
## using del keyword
del batter_detail_dict['bowling_style']
print("After deleting the key-value pair: ", batter_detail_dict, "\n")

## using pop() - pass the key to remove the key-value pair. The method returns the popped value
print(batter_detail_dict.pop('batting_pos'))

print(batter_detail_dict.pop('bowling_style', 'Unknown')) #if key not present - it raises KeyError. We can set a default value, to handle the error.

## using popitem() - pops and returns the last inserted key-value pair
print(f"The last item in {batter_detail_dict} is {batter_detail_dict.popitem()}")

## use of clear() - it empties a dictionary
tennis_p2.clear()
print(tennis_p2, '\n')
#------------------------------------------------------------------------------------

# Iterating through a dictionary:
for i in pkt_dictionary: 
    print(i) #prints the keys

# using .keys(): same output
for key in pkt_dictionary.keys():
    print(key)

# Iterating the values:
for value in tennis_p1.values():
    print(value, end = " -- ")

print()

# Iterating each key-value pair:
for item in batter_detail_dict.items():
    print(item)

#------------------------------------------------------------------------------------

# Other iterables' behaviors:
     
#len()
print(f"\nOur pocket dictionary currently has {len(pkt_dictionary)} words.")

#membership operation
print('nation' in tennis_p1)
print('Brimming' not in pkt_dictionary)

#------------------------------------------------------------------------------------

# Other methods in Dictionary:

## Get ~ If the key is not present, get() method doesn't throw any error, unlike [key].
print(pkt_dictionary.get('Brisk'))
print(pkt_dictionary.get('Buffled')) #will just return None

# ** incase we want a default value if the key is not present, that can be done too.
print(tennis_p1.get("favoured_hand", "Right")) # **It doesn't update the dictionary though.**
print(tennis_p1)


## Setdefault ~ works somewhat similar, with one distinction. If the key is not present, the new key adds an item. But, if the key is present, it doesn't update the dictionary.
tennis_p1.setdefault("my_fav", False) #--> no change to the dictionary, as key is present.
tennis_p1.setdefault("no_of_GS", 0) #--> no key present, sets a default value.
print(tennis_p1)


## Update ~ adds or replaces key-value pairs from another mapping or iterable.
online_dictionary = {'Brimming': "completely full, right up to the very top edge, or bursting with a heavy load of something",
           'chuffed': "very pleased, happy, or delighted about something"
}
pkt_dictionary.update(online_dictionary) #either overwrites the value of a Key, or adds an item if key not present.
print(pkt_dictionary)

print()

## copy ~ used to create a shallow copy of a dictionary
mini_dictionary = pkt_dictionary.copy()
mini_dictionary.popitem()
print(mini_dictionary) #last key-value pair removed
print(pkt_dictionary) #no changed to the original dictionary

## fromkeys ~ Creates a dictionary with the list of copies, and sets default value of None to each keys. A custom value can be set, but only one value across all keys
keys = ["name", "age", "profession", "salary"]
new_dict = dict.fromkeys(keys, None)
print(new_dict)
