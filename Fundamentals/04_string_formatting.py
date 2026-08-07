#Older syntax

w1 = "DO"
w2 = "BE"
print("To {} is to {}".format(w1, w2))

print("To {0} is to {1}".format(w1, w2)) #same
print("To {1} is to {0}".format(w1, w2))
print("Scooby Dooby Do!\n----------")


#since Python  v3.6

name = "Steyn"
country = "South Africa"
jersy = 8
print(f"{name} donned jersy no. {jersy} for {country}")


#numeric string formatting
print("{:.2f}".format(5.368394))


#Alignment using format
print("{:<10}".format(name)) #ljust
print("{:>10}".format(name)) #rjust
print("{:^10}".format(name)) #center
print()
print(f"{name:-<10}") #ljust
print(f"{name:.>10}") #rjust
print(f"{name:*^10}") #center
