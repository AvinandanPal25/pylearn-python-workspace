# for loop: Iterates element by element in an iterable (string, list, tuple, range, dictionary or set)

count = 0 #counter to track how many such numbers are there
for num in range(1,101):
    #print(f"Processing {num} -- ") #executes each time
    if num%3==0 and num%5==0: #the below code is executed only when True
        print(f"{num} is divisible by both 3, and 5.")
        count +=1

print(count)
print(num) #loop ends at num=100, as the last element of the range iterator is 100
print()

#-----------------------------------------------------------------------------------------------------------

# while loop: Executes the block of code until the entry-condition is true

num = 1
count = 0
while (num<=100):
    #print(f"Processing {num} -- ") #executes each time
    if num%3==0 and num%5==0: #the below code is executed only when True
        print(f"{num} is divisible by both 3, and 5.")
        count +=1
    
    num+=1 #to converge num to 101, the termination condition


print(f"{count} number(s), between 1 & 100, are divisible by both 3 and 5")
print(num) #num becomes 101, and then the entry continued fails, the program goes out of the loop
print()

# ** if the termination condition is never met, it results into an infinite loop.

#-----------------------------------------------------------------------------------------------------------

# break & continue
## `break` terminates the loop, and the program exits the loop body, while
## `continue` skips the current iteration (anything beyond it inside the loop), and moves to the next iteration

chat = "Call me b4 you leave." 
id = 0
while id<len(chat):
    if chat[id].isdigit():
        break #when digit is found, the loop is terminated
    print(chat[id], end=" ") # so prints: "C a l l  m e  b"
    
    id+=1

print()


leap_years = []
for year in range(1980, 2051):
    if year % 400 != 0 and (year % 4 != 0 or year % 100 == 0): #not a leap year condition
        continue

    print(year, "- is a leap year") #the line is not reached if continue is encountered, next iteration starts
    leap_years.append(year)

print(leap_years, "\n")

#-----------------------------------------------------------------------------------------------------------
# else in loop: Else block in loop gets executed only when the loop exits naturally. If `break` breaks it, else is not executed.
## Normally exits means ~ whether the iterable exhausts, or the entry-condition of while loop becomes false.

skills = ["Python", "Data Analysis", "API development", "ML", "MongoDB", "SQL", "AWS", "Java"]
# for skill in skills:
#     if skill.lower() == "c++":
#         print("Found")
#         break
#     else: print("Not Found")

# This won't work... it would print "Not Found" for each case when skill is not found in the list. 
# It is required to maintain a flag variable.

print("-"*20)

is_found = 0
for skill in skills:
    if skill.lower() == "c++":
        print("Found")
        is_found = 1
        break
if not is_found: print("Not Found")

print("+"*20)

# Alternative approach using `else`:
for skill in skills:
    if skill.lower() == "c++":
        print("Found")
        break
else: print("Not Found")  #since break is never encountered, else is executed

# ** Indentation matters in Python, as we are not using any brackets to segregate. 
#    The first and the last snippets are completely same, barring the indentation. It says where the `else` clause belongs to.

#Else with while loop:
id = 0
while id<len(skills):
    if skills[id].lower() == "c++":
        print("Found")
        break
    id+=1
else: 
    print("Not Found") 

#-----------------------------------------------------------------------------------------------------------
# Nested Loops: a loop inside another (inside another... and so on). For every iteration of the outer loop, the inner loop would iterate completely. 

colors = ("Red", "Blue", "Green")
sizes = ("S", "M", "L")

for color in colors:
    for size in sizes:
        print(color, size)

print()

# ** Break and Continue effects on the loop it is part of.
#    i.e. if a break statement is in the inner loop, the inner loop is broke, but the outer loop moves to its next iteration.
#    similarly, continue would skip the current iteration of the loop it is part of, and go to the next iteration.
        
for color in colors:
    for size in sizes:
        if f"{color}-{size}" == "Red-M": 
            print("---continue with next size---")
            continue
        
        print(color, size)       
        if f"{color}-{size}" == "Blue-S": 
            print("---Broken the whole color---")
            break

