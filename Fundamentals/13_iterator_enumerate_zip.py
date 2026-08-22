# ITERATOR

my_list = [25,17,16,5]
my_str = "Cillian Murphy"
my_tup = (2,12,8,11)
my_range = range(1,50,7)
my_dict = {"actor": "Brad Pitt", "age": 62, "best_movie": "Fight Club", 
           "other_movies": ["Meet Joe Black", "Se7en", "Troy", "World War Z", "Inglorious Basterds", "F1", "12 Monkeys"], 
           "next_movie": "Heart of the Beast"}
my_set = {"Salah", "Szoboszlai", "Diaz"}

for i in my_list:
    print(i)

for char in my_str:
    print(char)

for num in my_tup:
    print(num)

for val in my_range:
    print(val)

for item in my_dict.items():
    print(item)

for player in my_set:
    print(player)


'''Every iterables provides an iterator object for traversing through it. And whenever an item is required, it can produce that item. '''

set_iter = iter(my_set)

print(next(set_iter)) #Salah
print(next(set_iter)) #Szoboszlai
print(next(set_iter)) #Diaz
# print(next(set_iter)) # StopIteration ERROR 


'''It keeps track of the current item in an iterable. And it gets updated to the next item as the iterable is traversed.'''

list_iter = iter(my_list)

print(next(list_iter)) #25
for i in list_iter:
    print(i) # starts from 17, not 25


print()
# ------------------------------------------------------------------------------------------------------------------------------------

# ENUMERATE
    
lst = ["AP", "VK", "ABD", "JS"]

# Approach -1:
for i in range(len(lst)):
    print(i, lst[i])

print()

# Approach -2:
for i, item in enumerate(lst):
    print(i, item)


for i, item in enumerate(lst, start=101):
    print(i, item)

# print(list(enumerate(lst)))
print()
# ------------------------------------------------------------------------------------------------------------------------------------

# ZIP
    
num = [1,2,3,4,5]
string_num = ["One", "Two", "Three", "Four"]

# Approach -1:
for i in range(min(len(num), len(string_num))):
    print(f"{num[i]} - {string_num[i]}")

print()

# Approach -2:
for i, j in zip(num, string_num):
    print(f"{i} - {j}")

print()
# ------------------------------------------------------------------------------------------------------------------------------------

# RCB - 248/3 (20) vs GL, 2016, M Chinnaswamy Stadium - Scorecard

players = {"Gayle", "Kohli", "ABD", "Watson"}
scores = [6, 109, 129, 0]
balls = [13, 55, 52, 1]
sixes = (0,8,12,0)
fours = (1,5,10,0)


for position, (player, score, ball, four, six) in enumerate(zip(players, scores, balls, fours, sixes), start=1):
    print(f"Batter_{position}. {player}: {score}({ball}). [4s-{four}, 6s-{six}]")

print()
iterator = iter(enumerate(zip(players,scores,balls, fours,sixes), start=1))
print(next(iterator))
print(next(iterator))
print(next(iterator))
