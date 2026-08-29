# Create a list of squares of numbers between 1 and 6

squares = []
for num in range(1, 6):
    squares.append(num ** 2)

print(squares) # this is absolutely fine.

# But a more compact way of creating the same is -- 
squares2 = [num**2 for num in range(1,6)]
# This is LIST COMPREHENSION.
print(squares2)


# Not always a transformation is needed to be made
nums = [2,1,5,6,9]
copied_num = [num for num in nums]
print(copied_num)


#Comprehension with Filter condition:

odd_sq = [num**2 for num in range(1,10) if num%2==0]
print(odd_sq)

cities = ["Pune", "Hyderabad", "Delhi", "Bangalore", "Kolkata", "Mumbai"]
repeat_or_3peat = [s*2 if len(s)>5 else s*3 for s in cities]

print(repeat_or_3peat)

#------------------------------------
# SET COMPREHENSION
unique_remainders = {num%5 for num in (2,5,19,34,30,33,42)}
print(unique_remainders)


num_1 = [1,2,5,1,3,6,7,3,8]
num_2 = [1,4,9,1,4,9,8]

zipped_combo = {combo for combo in zip(num_1, num_2)}
print(zipped_combo)


#------------------------------------
# DICTIONARY COMPREHENSION
names = ["Jannik", "Virat", "de Villiers", "", "Mo Salah"]
name_len_dict = {name: len(name) for name in names if name != ""}
print(name_len_dict)