#sq_till_million = [i**2 for i in range(1,100001)] #is gonna exhaust a lot of memory. **Don't run this though.

sq_till_million = (i**2 for i in range(1,100001))
print(next(sq_till_million)) #1
print(next(sq_till_million)) #4
print(next(sq_till_million)) #9 ... and so on. 

# GENERATORS are lazy: Because a generator doesn't do a thing until you call next().

# YIELD:
def sq_generator_till_n(n):
    for i in range(1, n + 1):
        yield i*i

sq_till_million = sq_generator_till_n(100000) #it doesn't run the loop a million times, and produces the squares. 
                                              #It does nothing. Just creates a generator object (an iterable)

print(type(sq_till_million)) #<class 'generator'>

print(next(sq_till_million))
print()

#--------------------------------------------------------------------------------
# generator have state: it starts from where it had pause in the previous run
def print_n_yield():
    print("A")
    yield 10
    print("B")
    yield 20
    print("C")
    yield 30
    print("D")

print_n_yield() #doesn't do anything
pny = print_n_yield()
x=next(pny) #prints A, and x is 10
print(x)
x=next(pny) #prints B, and x is 20: Not "A"
print(x)

#----------------------------------------------------------

def add5_n_return():
    i = 1
    while True:
        i +=5
        return i

def add5_n_yield():
    i = 1
    while True:
        i +=5
        yield i

print()
#-------------------------------------------------------------------------------------

# RETURN VS YIELD: 
'''
add5_n_return() will return 6, and TERMINATE the function. You call it again, it would return 6 again.

# add5_n_yield() will do nothing. By calling next(), yield will produce 6. Then, the subsequent next() will produce 11, then 16, 22 and so on. So, yield produces and SUSPENDS the process, until it resumes, unless the generator is exhausted.

# return is "Take it. Goodbye!"
# yield is "Take it. Bye, see you tomorrow!"
'''

x = add5_n_return()
print(x) #6
x = add5_n_return()
print(x) #6
print()

x = add5_n_yield()
print(next(x)) #6
print(next(x)) #11
x = add5_n_yield()
print(next(x)) # a new generator obj: prints 6 again.

print()
#----------------------------------------------------------

# For a Generator to produce results, the Yield statements has to be reached
def add5_n_yield(i):
    i = i+5
    yield i
    print(f"5 added to {i}")
    yield i
    print(f"5 added to {i} again")

process = add5_n_yield(i=2)
for _ in range(3):
    x = next(process)
    print(x, "\n........................")

'''first iteration: x = 7
second iteration: 5 added to 2; x = 7 (no changes made to i)
third iteration: 5 added to 2 again -- then, StopIteration error, cause no more yield.'''

#--------------------------------------------------------------------------------

# REAL WORLD USAGE OF GENERATOR: