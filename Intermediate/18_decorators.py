def decor(func):
    def wrapper():
        print("Hello.")
        func() #wrapper func has scope of func() --> closure
        print("See you soon, bye!!!")

    return wrapper


def greet():
    print("Good Morning! How are you?")

greet = decor(greet) 
#decorator creation - func passed as argument: a function being a "first class object"

greet()
print()


@decor
def greet2():
    print("Good Evening! Where are you heading towards?")

#greet = log_function(greet) 
#no longer reqd. @decor means exactly this line.

greet()
greet2() #the exact same name is to be used.
print()

#---------------------------------------------------------------------------