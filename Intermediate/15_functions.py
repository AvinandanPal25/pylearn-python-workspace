# WHY DO FUNCTIONS EXIST?

names = ["Sinner", "Kohli", "aBd", "SALAH"]
uppercased_names = []
for name in names:
    upper_name = ""
    for c in name:
        if ord(c)>90:
            upper_char = chr(ord(c)-32)
        else:
            upper_char = c
        upper_name = upper_name+upper_char
    uppercased_names.append(upper_name)

print(uppercased_names)
#-------------------------------------------
uppercased_names_2 = []
for name in names:
    uppercased_names_2.append(name.upper()) #Built in method of Str object -- can be used whereeve needed instead repeating the above code

print(uppercased_names_2)
#-------------------------------------------

def my_custom_upper_func(string):
    upper_string = ""
    for c in string:
        if ord(c)>90:
            upper_char = chr(ord(c)-32)
        else:
            upper_char = c
        upper_string = upper_string+upper_char

    return upper_string

uppercased_names_3 = []
for name in names:
    upper_name = my_custom_upper_func(name) #function call, and reusability
    uppercased_names_3.append(upper_name)

print(uppercased_names_3)


print(my_custom_upper_func)  #does not execute the func because of missing parenthesis.
print()

#----------------------------------------------------------------
# Keyworded Arguments:  e.g. Calculate simple interest
def calc_si(principal, int_rate, n_year):
    print(f"Principal amt of {principal}")
    print(f"Interest rate = {int_rate}")
    interest = principal*int_rate*n_year/100
    print(f"After {n_year} year(s), the Simple Interest would be Rs.{interest}")
    return principal+interest

print("Total amount to return - Rs.", calc_si(10000, 5, 2))
print()
print("Total amount to return - Rs.", calc_si(n_year=10, principal= 50000, int_rate = 8))

# print("Total amount to return - Rs.", calc_si(50000)) #error as all arguments are not passed

#----------------------------------------------------------------
# Default Paramters:
def calc_ci(principal, n_year, int_rate = 10): #default parameters should only be place after all the non-default parameters
    print(f"Principal amt of {principal}")
    print(f"Interest rate = {int_rate}")
    total = round(principal*((1+int_rate/100)**n_year),2)
    cmpd_interest = total-principal
    print(f"After {n_year} year(s), the Compound Interest would be Rs.{cmpd_interest}")
    return total

print("Total amount to return - Rs.", calc_ci(10000, 5, 2))
print("Total amount to return - Rs.", calc_ci(10000, 5)) #int_rate not passed --> default int_rate of 10 is used.
print("Total amount to return - Rs.", calc_ci(n_year=10, principal=300000)) #keyworded argument is still possible.

#----------------------------------------------------------------

# *args and **kwargs --> For variable length arguments, args holds all the positional arguments as a Tuple. While, kwargs holds all the keyworded arguments as a list.

def func_with_variable_length_parameters(*args, **kwargs):
    for i in args:
        print(i)

    for j in kwargs:
        print(j)

    print(args) # a tuple
    print(kwargs) # a dictionary

func_with_variable_length_parameters(2,3,1,"Dale", True, name="Jannik", age=23, profession="Tennis Player")


def sum_values(*numbers):
    total = 0
    for i in numbers:
        total=total+i

    return total

print(sum_values(1,2))
print(sum_values(5))
print(sum_values(7,19,3,53))
print(sum_values())


# mix of all
def student_report_card(name, *marks_obtained, gender="male", **details):
    print(f"{name}({gender[0].upper()}) - roll_no. {details.get('roll_no')}")
    print(f"Obtainted marks: {marks_obtained}")
    print(f"Info about the student: {details}")

    total_marks = 0
    for mark in marks_obtained:
        total_marks = total_marks+mark

    avg = round(total_marks/len(marks_obtained),1)
    print(f"Average marks: {avg}")
    print("Passed" if avg>30 else "Failed\n")

student_report_card("Adrit",93,95,87,83,91,79,92, gender="male", of_class = 'X', roll_no = 1, 
                    extra_curricular = ["Plays Cricket", "Class Monitor", "Does NCC", "Knows Drawing"])
student_report_card("Akankha",83,75,97,99, gender="female", of_class = 'XII', extra_curricular = ["Sings Song"], appearing_for = "JEE")


# Unpacking: * and ** has a related but opposite meaning when used in function call. It then unpacks the arguments as below.

obtained_marks = [93,95,87,83,91,79,92]
std_details  = {"of_class" : 'X', "roll_no" : 1, "extra_curricular" : ["Plays Cricket", "Class Monitor", "Does NCC", "Knows Drawing"]}
student_report_card("Adrit",*obtained_marks, gender="male", **std_details) #same result... way of passing the arguments is different.
