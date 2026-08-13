# Conditional statements:~

# If statement: if the to-be-evaluated condition(s) result in True: the block works
age = int(input("What is your age?"))
if age>18:
    print("You are eligible to give vote.")

# If-Else Statement:
marks = [75, 89, 72, 92, 87, 93]
if round(sum(marks)/len(marks),2)>55:
    print("You are above cut-off.")
else:
    print("Below cut-off, you are not qualified.")

# If-Elif-Else ladder:
avg_mark = round(sum(marks)/len(marks),2)
if avg_mark>95: print("AA - Outstanding")
elif avg_mark>90: print("Grade - A")
elif avg_mark>75: print("Grade - B")
elif avg_mark>60: print("Grade - C")
elif avg_mark>50: print("Grade - D")
elif avg_mark>30: print("Grade - E")
else: print("Failed.")

# Nested If-else:
years = range(1900, 2101, 10)
for y in years:
    if y%100:
        if y%4:
            print(f"{y} is not a leap year!")
        else:
            print(f"{y} is a leap year!")
    elif y%400==0:
        print(f"{y} is a leap year!")
    else:
        print(f"{y} is not a leap year!")
print()


#------------------------------------------------------------------------------------------
        
# Boolean operators: AND - OR - NOT:- Instead of using long and deeply nested if-else block, boolean operator can be used to combine conditions
## AND - requires all the conditions to yield true or truthy value
## OR  - requires at least one of the conditions to be true or truthy
## NOT - reverses the Boolean value of a condition
        
# --> If the design, color and build of the shoe suits me -- I would buy the shoe if it is under 1k, and rated above 4. 
#     If I liked it but above 1k, and rating equal or above 4.5: I will buy. 
#     If I liked it, above 1k, but rating between 3-4.5: I will wishlist it. If rating below three, discard.
#     If I don't like it, always discard.

# Using nested if else
i_like_it = True
shoe_price = 956
rating = 3

if i_like_it: 
    if shoe_price<1000:
        if rating>4: print("Buy the shoe!")
        else: print("Discard")
    
    else:
        if rating>=4.5: print("Buy the shoe!")
            
        else: 
            if rating>=3:
                print("Wishlist & monitor")
            else:
                print("Discard")

else: print("Discard")

# Using Boolean Operator to combine conditions:
if not i_like_it: #not operator
    print("Discard")
else:
    if (shoe_price<1000 and rating>4) or (shoe_price>1000 and rating>=4.5) :  print("Buy the shoe!") #and & or
    elif (shoe_price>1000 and rating>=3 and rating<4.5): print("Wishlist & monitor")
    else: print("Discard")

print()


# Short Circuit Operation:
''' Boolean operators do not always return True of False
`and` returns the first falsy value. If none are falsy, it returns the last operand.
`or` returns the first truthy value. If none are truthy, then returns the last operand.

This way, when the first falsy or truthy value if found, rest of the conditions are not even checked.
'''    
print(True and True and "Hi" and 20 and []) #[]
print(True and True and "Hi" and 20 and [2]) #[2]
print(True and False and "" and 20 and [2]) #False
print(True or False or "Hi" or 18) #True
print(False or False or "Hi" or 18) #"Hi"
print(False or False or "") #""
print(17 and 18) #18
print(17 or 18) #17
print(0 and 25) #0
print(0 or 25) #25
print(0 or 0) #0

## ** Operator Precedence: not --> and --> or. A parenthesis can override the precedence.

#USE CASE:
usernames = ["foxy", "big_elph", "lion_king", "dippo_hippo"]
user_input = input("Enter your username:")
if(user_input not in usernames): user_input=None
user = user_input or "Guest"

print(f"Welcome - {user}")
#------------------------------------------------------------------------------------------

# Chaining comparisons: age>18 and age<60 is same as 18<age<60

# Ternary Operator:
# if shoe_price>1000:
#     decision = "Wishlist"
# else: decision = "Buy it!"
decision = "Wishlist" if shoe_price>1000 else "Buy it"

#can be nested further, but when complex situation arrives, the simple if else block structure is recommended.

#------------------------------------------------------------------------------------------

# Match - case: require Python 3.10 or above.

response, status_code = [(1, "Virat Kohli", "Batter"), (2, "Brad Pitt", "Actor"), (3, "Matthew Mole", "Singer")], 200

## 1. Simple matching
# match status_code:
#     case 200:
#         print("API request Successful")
#     case 404: 
#         print("Data Not Found")
#     case 400: 
#         print("Bad Request")
#     case _:
#         print("Internal Server Error")

# ## 2. Combining Multiple Patterns:
# user_role = "Editor"
# match user_role.lower():
#     case "admin" | "super_admin":  #admin or super_admin
#         print("Full Access")
#     case "editor" | "moderator":
#         print("Limited Access")
#     case _:
#         print("Read Only Access")

# ## 3. Matching Sequence:
# point = (0, 5)

# match point:
#     case (0, y):
#         print(f"On Y-axis, at y={y}")
#     case (x, 0):
#         print(f"On X-axis, at x={x}")
#     case (x, y):
#         print(f"Point at ({x}, {y})")
#     case _:print("Incorrect 2D point format")

# for r in response:
#     match r:
#         case (id, name, "Batter"):
#             print(f"#{id}: {name} plays Cricket.")
#         case (id, name, "Singer"):
#             print(f"#{id}: {name} sings songs")
#         case(id, name, "Actor"):
#             print(f"#{id}: {name} acts in Movies.")
#         case _:
#             print("Unknown profession")