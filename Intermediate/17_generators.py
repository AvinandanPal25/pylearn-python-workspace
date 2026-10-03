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
    print(f"Saying it again, 5 added to {i}")

process = add5_n_yield(i=2)
# for _ in range(3):
#     x = next(process)
#     print(x, "\n........................")

'''first iteration: x = 7
second iteration: 5 added to 2; x = 7 (no changes made to i)
third iteration: 5 added to 2 again -- then, StopIteration error, cause no more yield.'''


#------------------------------------------
# Yield with return: Instead of producing values using next(), a loop can traverse through each produced value as well.

def demo():
    yield 10
    yield 20
    return 30

print(demo())

for x in demo():
    print(x) # On the third next(), the generator executes return 30, 
             # which terminates the generator by raising StopIteration whose value is 30. 
             # Since `for` handles StopIteration automatically, 30 isn't exposed by the loop.
print()


# yield from :- this can be used to yield values from another generator/ an iterable
def subprocess(n):
    x = 0
    while x<n: 
        yield x
        x+=1

def main_process(n):
    yield from subprocess(n) #yields items one by one from another generator

print(list(main_process(10)))
print()

def yield_from_example():
    yield from [1, 2, 3]  # Loops and yields items from an iterator: 1 --> 2 --> 3
    yield 4

for item in yield_from_example():
    print(item)

'''
Output:
1
2
3
4

Instead, if yield is used in line #132 (i.e. yield [1,2,3]) --> output would be
[1,2,3]
4
'''
print()

#-----------------------------------------------------------
# The generator has its own local namespace.
s = subprocess(5)
print(next(s)) #x=0 
print(next(s)) #increments to 1, x=1 is yielded
x = 10
print(next(s)) #x from inside the generator func is still 1, which is incremented to 2, x=2 is yieled.
print()

#----------------------------
# but a mutable object can be modified.
def subprocess_2(n):
    x = 0
    nums = []
    while x<n: 
        nums.append(x)
        yield nums
        x +=1

s2 = subprocess_2(5)
print(next(s2)) #this is printing [0]
nums = next(s2)
print(nums)
nums.append(99) #modifies the mutable object 99 is appened after 1.
nums = next(s2) #[0, 1, 99, 2]
print(nums)
print("-"*30)

#------------------------------------------------------------------
#closing a generator, sending value to generator, and a practical example.
def first():
    yield "First generator is Ready"
    yield 20

f = first()
print(next(f)) #10
f.close() #generator is closed
# print(next(f)) #stopIteration error.
print()

def second():
    total = yield "Second generator is Ready"
    yield total * 2

def main():
    for i in first():
        result = i

    print("First generator ended with: ", result)

    g = second() #starts the second sub-generator: at this point yield is not reached yet
    #so can't send a value yet other than None

    print(next(g)) #or call next to reach yield --> "Second generator is Ready"

    value = g.send(result)#by sending result, the value 20 is received at line 188 by total
    print("Second generator yields: ", value) #yields 20*2 = 40

main()

#--------------------------------------------------------------------------------
# Generator Pipeline:
# `yield from` was implicitly working in a loop, and yielding from another generator or iterator.
# But here we are running a generator, every time another generator yield a value --> a pipeline of sort.

def numbers():
    for i in range(5):
        yield i


def log_generator(gen):
    for value in gen:
        print("Produced:", value)
        yield value

g = numbers()

for x in log_generator(g):
    print("Consumer got:", x) # if the yield value line was not used, this line would have never executed as the loop on gen would have exhausted itself.

'''by using that yield, the value is yielded and sent back out of the loop, inside the loop on log_generator.... 
and prints `consumer got`; and then the for loop would have gone inside the `for value in gen loop` again, 
and executed the 2nd iteration.
The yield is essentially the handoff point.'''






#--------------------------------------------------------------------------------
# REAL WORLD USAGE OF GENERATOR:
## Usecase: There is a potentially large or ongoing source of data, and I don't need all of it at once. -> Use generators

'''Ex. 1: Suppose you have a 20 GB log file.
data = file.read() is not efficient cause it asks Python to load a huge size of data.
Using Generators and yield functionality, we never need 20GB of memory.
'''

def strip_n_transform_line(line):
    pass 

def read_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line

for line in read_lines("server.log"):
    strip_n_transform_line(line) 


'''Ex. 2: Data-processing pipelines.
Using Generators we can build a broad pipeline (similar to what was demonstrated earlier).
Instead of do all the operators one after the other, and thereby use up memory, using pipelined-generators... 
one single record can be completed, and then continue with the next one.
'''
def read_records():
    pass
def valid(rec):
    pass
def normalize(rec):
    pass
def make_features(rec):
    pass
def load_data(rec):
    pass

def clean(records):
    for record in records:
        if valid(record):
            yield normalize(record)

def extract_features(records):
    for record in records:
        yield make_features(record)

records = read_records()
cleaned = clean(records) #records is a generator, not data yet.
features = extract_features(cleaned) #cleaned is also a generator, and has no data yet.

for row in features: #here extract_features starts, and calls for data from cleaned, 
                     #which then calls data from clean, which fetches from read_records. 
                     #The normalized value is yielded, and is received by extract_features, 
                     #which yields data using make_features func. And then the next loops starts.
    load_data(row)


'''EX. 3: API Handling.
Suppose an API gives you data when you request it with request params and page no.
Now, if we do it without generators, we might use a loop to iterate over a page index, and capture all data into one list or dictionary.
And at the end of that loop is that we would have the whole data.
Using Generators, we can get the data and process it for one set of row at a time, without needing to store the value somewhere.'''

def prepare_report(customer):
    pass

def send_email(report):
    pass

#without generators ---
all_customers = []
pages = range(1,1001)
import requests
for page in pages:
    response = requests.get(
            "https://api.example.com/customers",
            params={"page": page, "limit": 100}
        )
    data = response.json()["data"]
    if not data:
        print(f"No response received for page-{page}!")
        continue

    all_customers.extend(data)  #data of 1000 pages

for cust in all_customers: #a loop of maybe million/billion customer in 1000 pages.
    cust_report = prepare_report(cust)
    send_email(cust_report)

#usage of generators ---
def get_customers():
    page = 1

    while True:
        response = requests.get(
            "https://api.example.com/customers",
            params={"page": page, "limit": 100}
        )

        data = response.json()["data"]
        if not data:
            print(f"No response received for page-{page}!")
            continue

        for customer in data:
            yield customer

        page += 1

for customer in get_customers():
    cust_report = prepare_report(cust)
    send_email(cust_report)

#==============================================================================================================================================================================================================
# NB: If we need the whole data at once, generators isn't required. But if we want to process something per data, we can use generator and process that once, and move to the next one.
    # Especially when: result sets are large, API pagination is involved, processing is expensive, you can process records independently, OR you want to start processing before the entire data arrives.